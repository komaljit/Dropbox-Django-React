from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import File, Folder
from rest_framework.authtoken.models import Token


# decorator to generate token when a user signup
def generate_token(user):
    Token.objects.create(user = user)


class SignupSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('username','password','first_name','last_name','last_login')
        extra_kwargs = {'password':{'write_only':True},'last_login':{'read_only':True}}

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        user_obj = User(
            username=username,
            first_name=first_name,
            last_name=last_name
        )
        user_obj.set_password(password)
        user_obj.save()
        Folder(folder_path=username, username=user_obj)    # creating a virtual base folders to track user files
        generate_token(user_obj)
        return validated_data


class UpdateSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def update(self, instance, validated_data):
        print(instance)
        username = validated_data['username']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        user_obj = User(
            username = username,
            first_name = first_name,
            last_name = last_name
        )
        user_obj.set_password(password)
        user_obj.save()
        generate_token(user_obj)
        return validated_data


class LoginSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password')


class UserDetailSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('username','first_name','last_name','last_login')


class FolderSerializer(ModelSerializer):

    class Meta:
        model = File, Folder
        fields = ('filename','file', 'folder_path', 'username')


class FileUploadSerializer(ModelSerializer):

    class Meta:
        model = File
        fields = ('filename','file','folder_path', 'username')
        # extra_kwargs = {'username': {'read_only': True}}


class FileDeleteSerializer(ModelSerializer):

    class Meta:
        model = File
        fields = ('filename','file')
        extra_kwargs = {'username': {'read_only': True}}


class MakeFolderSerializer(ModelSerializer):

    class Meta:
        Model = Folder
        fields = ('foldername', 'folder_path')