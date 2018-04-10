from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, CharField
from django.contrib.auth.models import User



class LoginSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password')

class UserListSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password')







