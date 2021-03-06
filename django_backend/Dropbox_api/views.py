from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.views import APIView, status
from .models import File, Folder
from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.views.static import serve
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import (LoginSerializer, SignupSerializer, UpdateSerializer,UserDetailSerializer,
                          FolderSerializer, FileUploadSerializer, MakeFolderSerializer)


# decorator to generate token when a user signup
def generate_token(fun):
    def wrapper(*args):
        serializer = args[1]
        user = User.objects.filter(username=serializer.data['username'])
        Token.objects.create(user = user)
        return fun(*args)
    return wrapper


# In case I want to add token authentication in Dropbox app in the future
# function to get token
def get_token(user):
    return Token.objects.get_or_create(user=user)


# View for login
class LoginAPI(APIView):
    serializer_class = LoginSerializer
    authentication_classes = (SessionAuthentication, )

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        if user:
            return Response({"user": str(user)}, status=200)
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


# view for signup
class SignupAPI(CreateAPIView):
    serializer_class = SignupSerializer


# view for obtaining user detail
class UserDetailsView(RetrieveAPIView):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = UserDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer_class()
        serializer_data = serializer(instance)
        return Response(serializer_data.data)

    def get_object(self):
        user = self.request.user
        return User.objects.get(username=user)


class UpdateUserAPI(UpdateAPIView):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateSerializer


# view for deleting a account
class DeleteUserApiView(APIView):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)

    def delete(self, request):
        user_obj = User.objects.get(username=request.user)
        print("user is deleted" + str(request.user))
        user_obj.delete()
        return Response(status=204)


# view for logout
class LogoutView(APIView):
    serializer_class = LoginSerializer

    def get(self, request):
        logout(request)
        return Response(status=204)


# view for handling file uploads
class FolderApiView(APIView):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = FolderSerializer

    # get list of files
    def get(self, request, *args, **kwargs):
        folder = str(request.user) + '/'
        if request.data.get('folder_path'):
            folder += request.data.get('folder_path')
        folder = Folder.objects.get(folder_path=folder)
        files = File.objects.filter(folder_path=folder)
        child_folders = Folder.objects.filter(folder_parent=folder)
        serialized_data = self.serializer_class(files, many=True)
        return Response(serialized_data.data, status=200)


# view for handling uploading of a file
class FileUploadAPIView(APIView):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = FileUploadSerializer

    def post(self, request):
        return self.create(request)

    def create(self, request):
        # print(request.data.get('folder_path'))
        folder = Folder.objects.get(folder_path=request.data.get('folder_path'))
        request.data['folder_path'] = folder
        serializer = self.serializer_class(data=request.data)
        print(serializer)
        if serializer.is_valid(raise_exception=Response(status=400)):
            serializer.save()
            return Response(status=204)


class DownloadFileApiView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)
    lookup_field = 'filename'

    def get(self, request, *args, **kwargs):
        print(self.kwargs[self.lookup_field])
        file_path = settings.MEDIA_ROOT
        return serve(request, path=self.kwargs[self.lookup_field], document_root=file_path)


# view for deleting a file
class DeleteFileApiview(DestroyAPIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (SessionAuthentication, )
    lookup_field = 'filename'

    def destroy(self, request, *args, **kwargs):
        print(kwargs['filename'])
        instance = get_object_or_404(File, file=kwargs['filename'])
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


# view to make folder
class MakeFolderApiview(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)
    serializer_class = MakeFolderSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
