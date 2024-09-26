from rest_framework import serializers
from ..models import PriceList

class Currencyserializers(serializers.ModelSerializer):
    class Meta:  # Capitalize Meta
        model = PriceList  # Use equals sign for assignment
        fields = '__all__'