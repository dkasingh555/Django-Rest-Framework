from rest_framework import serializers
from ..models import Review

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'  # or list the specific fields you want to include
