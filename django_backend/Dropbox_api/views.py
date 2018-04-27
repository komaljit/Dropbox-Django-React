from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.views import APIView, status
from .models import File
from rest_framework.response import Response
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import (LoginSerializer, SignupSerializer, UpdateSerializer,
                          FileListSerializer, FileUploadSerializer)


# decorator to generate token when a user signup
def generate_token(fun):
    def wrapper(*args):
        serializer = args[1]
        user = User.objects.filter(username=serializer.data['username'])
        Token.objects.create(user = user)
        return fun(*args)
    return wrapper


# function to get token
def get_token(user):
    return Token.objects.get_or_create(user=user)


# View for login
class LoginAPI(APIView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return Response(status=204)
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


# view for signup
class SignupAPI(CreateAPIView):
    serializer_class = SignupSerializer
    permission_classes = (AllowAny,)


class UpdateUserAPI(UpdateAPIView):
    authentication_classes = (TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateSerializer


class DeleteApiView(APIView):
    authentication_classes = (TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def delete(self, request):
        user_obj = User.objects.filter(username='koml')
        # print(request.user)
        user_obj.delete()
        return Response(status=204)


# view for logout
class logoutView(APIView):
    serializer_class = LoginSerializer

    def get(self, request):
        logout(request)
        return Response(status=204)


# view for handling file uploads
class FileListApiView(APIView):
    authentication_classes = (TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = FileListSerializer

    # get list of files
    def get(self, request, *args, **kwargs):
        print(request.user)
        queryset = File.objects.filter(username= request.user)
        print(queryset)
        serializer = FileListSerializer(queryset, many=True)
        return Response(serializer.data, status=200)


class FileUploadAPIView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = FileUploadSerializer

    def post(self,request):
        return self.create(request)

    def create(self, request):
        file_obj = File(filename = request.data.get('filename'),
                        file = request.FILES['file'],
                        username = request.user)
        file_obj.save()
        return Response(status=204)
