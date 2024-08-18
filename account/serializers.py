from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.core.exceptions import ValidationError
class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already in use.")
        return value
    
    def create(self,validated_data, ):
        user = User.objects.create_user(
            email = validated_data['email'],
            username = validated_data['username'],
            
            password = validated_data['password']
        )
        return user
    

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  ['email','username','password']