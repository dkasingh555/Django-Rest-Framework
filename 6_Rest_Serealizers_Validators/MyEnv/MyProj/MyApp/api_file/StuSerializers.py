from rest_framework import serializers
from ..models import Studentlist

# def alphanumeric(value):
#     if not str(value).isalnum():
#         raise serializers.ValidationError("Only alphanumeric characters are allowed")

def alphanumeric(value):
    try:
        int_value = int(value)
    except ValueError:
        raise serializers.ValidationError("Only integer characters are allowed")
    
    if not str(int_value).isdigit():
        raise serializers.ValidationError("Only integer characters are allowed")


class StudentSerializers(serializers.Serializer):
    Stu_Name=serializers.CharField(max_length=100)
    Stu_Fname=serializers.CharField(max_length=100)
    Stu_Class=serializers.IntegerField(validators=[alphanumeric])
    Stu_Email=serializers.EmailField()
    Stu_Fee=serializers.DecimalField(max_digits=9, decimal_places=2)
    
    

    def create(self, validated_data):
        return Studentlist.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.Stu_Name=validated_data.get('Stu_Name',instance.Stu_Name)
        instance.Stu_Fname=validated_data.get('Stu_Fname',instance.Stu_Fname)
        instance.Stu_Class=validated_data.get('Stu_Class',instance.Stu_Class)
        instance.Stu_Email=validated_data.get('Stu_Email',instance.Stu_Email)
        instance.Stu_Fee=validated_data.get('Stu_Fee',instance.Stu_Fee)
        instance.save()
        return instance
        
    def validate_Stu_Fee(self, value):
        if value <=20000.00:
            raise serializers.ValidationError("Fee should be greater than 20000")
        return value

    def validate(self, data):
        if data['Stu_Name']==data['Stu_Fname']:
            raise serializers.ValidationError("Name and Father's name should be different")
        return data





