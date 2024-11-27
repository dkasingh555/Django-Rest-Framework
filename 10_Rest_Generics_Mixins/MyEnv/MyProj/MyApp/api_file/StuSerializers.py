from rest_framework import serializers
from ..models import Studentlist,Review

class StudentSerializers(serializers.Serializer):
    Stu_Name=serializers.CharField(max_length=100)
    Stu_Class=serializers.IntegerField()
    Stu_Email=serializers.EmailField()

    def create(self, validated_data):
        return Studentlist.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.Stu_Name=validated_data.get('Stu_Name',instance.Stu_Name)
        instance.Stu_Class=validated_data.get('Stu_Class',instance.Stu_Class)
        instance.Stu_Email=validated_data.get('Stu_Email',instance.Stu_Email)
        instance.save()
        return instance
        









