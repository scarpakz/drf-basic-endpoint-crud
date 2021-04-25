from rest_framework import serializers
from django.contrib.auth.models import User
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token
from .models import (
    Profile,
)

class CustomLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

class CustomRegistrationSerializer(RegisterSerializer):
    username = serializers.CharField(required=False)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    mobile_number = serializers.CharField(max_length=20)
    email = serializers.EmailField(required=True)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'mobile_number', 'email', 'password1', 'password2']

    def get_cleaned_data(self):
        return {
            'mobile_number': self.validated_data.get('mobile_number', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', '')
        }