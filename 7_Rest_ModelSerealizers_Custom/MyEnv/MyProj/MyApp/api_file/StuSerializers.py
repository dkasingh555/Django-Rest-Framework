from rest_framework import serializers
from ..models import Studentlist

class StudentSerializers(serializers.ModelSerializer):
  
   
   class Meta:
    model = Studentlist
    fields = '__all__'
    
    def create(self, validated_data):
        return Studentlist.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.Stu_Name=validated_data.get('Stu_Name',instance.Stu_Name)
        instance.Stu_Class=validated_data.get('Stu_Class',instance.Stu_Class)
        instance.Stu_Email=validated_data.get('Stu_Email',instance.Stu_Email)
        instance.Stu_Fee=validated_data.get('Stu_Fee',instance.Stu_Fee)
        instance.save()
        return instance
        









