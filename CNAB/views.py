from django.shortcuts import render

from .models import CNAB
from .forms import FormFile
from .serializers import CNABSerializer

from django.core.files.storage import FileSystemStorage


def upload_function(request):

    context = {}
    storage = FileSystemStorage()

    CNAB.objects.all().delete()

    if request.method == 'POST':
        form = FormFile(request.POST, request.FILES)
        context['form'] = form

        if form.is_valid():
            file = request.FILES['file']
            file_name = storage.save(file.name, file)

            with open(f"upload/{file.name}", "r", encoding="utf-8") as destination:
                row = destination.readlines()
                alist = ordered_list(row)
                if alist:
                    context['url'] = storage.url(file_name)
                else:
                    context['error'] = "Error while uploading file"
    else:
        form = FormFile()
        context['form'] = form
    return render(request, 'app/file_form.html', context)


def ordered_list(alist):
    for row in alist:
        type = row[:1]
        date = row[1:9]
        value = int(row[9:19]) / 100.00
        cpf = row[19:30]
        card = row[30:42]
        hour = row[42:48]
        owner = row[48:62]
        name = row[62:80]

        cnab_dict = {
            'type': type,
            'date': date,
            'value': value,
            'cpf': cpf,
            'card': card,
            'hour': hour,
            'owner': owner,
            'name': name
        }
        serializer = CNABSerializer(data=cnab_dict)
        if serializer.is_valid():
            serializer.save()

    return serializer


def get_filter_cnab(name):
    return CNAB.objects.filter(name=name)


def get_total_balance(name):
    total_balance = 0
    filter = get_filter_cnab(name)
    for item in filter:
        if item.type == 2 or item.type == 3 or item.type == 9:
            total_balance -= int(float(item.value))
        else:
            total_balance += int(float(item.value))

    return total_balance

def get_cnab(request, name):
    cnab = get_filter_cnab(name)
    total_balance = get_total_balance(name)
    return render(request, 'app/transaction.html', {'total_balance': total_balance, 'cnab': cnab, 'name': name})

