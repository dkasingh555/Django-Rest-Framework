from rest_framework import serializers
class Carserializers(serializers.Serializer):
    id=serializers.CharField(read_only=True)
    name=serializers.CharField()
    desc=serializers.CharField()
    status=serializers.BooleanField(read_only=True)
    
