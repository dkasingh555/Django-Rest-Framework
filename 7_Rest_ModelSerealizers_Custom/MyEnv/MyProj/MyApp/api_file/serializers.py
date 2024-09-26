from rest_framework import serializers
from ..models import Carlist
class Carserializers(serializers.ModelSerializer):
    discounted_Fee=serializers.SerializerMethodField()
    class Meta:
        model = Carlist
        fields = '__all__'

    def get_discounted_Fee(self,obj):
        Fee=obj.price-500
        return Fee