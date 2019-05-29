from rest_framework import serializers
from .models import UserData

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserData
        fields='__all__'

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserData
        fields=['first_name','last_name','age']