from django.db import models
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, MaxLengthValidator


class CNAB(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    type = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(9)])
    date = models.TextField(max_length=8, validators=[
                            MinLengthValidator(8), MaxLengthValidator(8)])
    value = models.TextField(max_length=10)
    cpf = models.TextField(max_length=11, validators=[
                           MinLengthValidator(11), MaxLengthValidator(11)])
    card = models.TextField(max_length=12, validators=[
                            MinLengthValidator(12), MaxLengthValidator(12)])
    hour = models.TextField(max_length=6, validators=[
                            MinLengthValidator(6), MaxLengthValidator(6)])
    owner = models.TextField(max_length=14)
    name = models.TextField(max_length=19)