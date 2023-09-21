from rest_framework import serializers
from .models import Combination, APIData

class APIDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIData
        fields = '__all__'