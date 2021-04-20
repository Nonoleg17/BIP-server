from rest_framework import serializers
from .models import PersonalData


class PersonalDataDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalData
        fields = '__all__'


class PersonalDataViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalData
        fields = '__all__'
