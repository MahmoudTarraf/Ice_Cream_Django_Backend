from rest_framework import serializers

from .models import IceCreamModel


class IceCreamSerializer(serializers.ModelSerializer):
    class Meta:
        model=IceCreamModel
        fields = '__all__'