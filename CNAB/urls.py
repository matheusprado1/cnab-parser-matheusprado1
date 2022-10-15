from django.urls import path
from . import views


urlpatterns = [
    path('operations/', views.upload_function, name='upload_file'),
    path('operations/<str:name>', views.get_cnab, name='get_cnab'),
]