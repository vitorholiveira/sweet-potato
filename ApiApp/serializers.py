from rest_framework import serializers 
from .models import Muscles, Exercice

class MusclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Muscles
        fields = '__all__'

class ExerciceSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Exercice
        fields = '__all__'