from rest_framework import serializers
from .models import SpecialOfferModel

class SpecialOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialOfferModel
        fields = '__all__'