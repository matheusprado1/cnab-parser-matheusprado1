from rest_framework import serializers

from .models import CNAB


class CNABSerializer(serializers.ModelSerializer):
    class Meta:
        model = CNAB
        fields = '__all__'
        extra_kwargs = {"id": {"read_only": True}}