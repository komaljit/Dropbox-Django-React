from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, CharField
from django.contrib.auth.models import User


class SignupSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('username','password','email','first_name','last_name','last_login')
        extra_kwargs = {'last_login':{'read_only':True}}


class LoginSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password')

class UserListSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password')







