from rest_framework import serializers
from ..models import Schoollist

class SchoolSerializers(serializers.ModelSerializer):
    class Meta:
        model = Schoollist
        fields = "__all__"
  
   