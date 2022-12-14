# Generated by Django 4.1.2 on 2022-10-14 21:04

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CNAB',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9)])),
                ('date', models.TextField(max_length=8, validators=[django.core.validators.MinLengthValidator(8), django.core.validators.MaxLengthValidator(8)])),
                ('value', models.TextField(max_length=10)),
                ('cpf', models.TextField(max_length=11, validators=[django.core.validators.MinLengthValidator(11), django.core.validators.MaxLengthValidator(11)])),
                ('card', models.TextField(max_length=12, validators=[django.core.validators.MinLengthValidator(12), django.core.validators.MaxLengthValidator(12)])),
                ('hour', models.TextField(max_length=6, validators=[django.core.validators.MinLengthValidator(6), django.core.validators.MaxLengthValidator(6)])),
                ('owner', models.TextField(max_length=14)),
                ('name', models.TextField(max_length=19)),
            ],
        ),
    ]
