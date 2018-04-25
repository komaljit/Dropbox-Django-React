from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.views import APIView, status
from .serializers import (LoginSerializer, SignupSerializer,
                          FileSerializer, FileUploadSerializer)
from .models import File
from rest_framework.response import Response
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.core.files.base import ContentFile

# decorator to generate token when a user signup
def generate_token(fun):
    def wrapper(*args):
        serializer = args[1]
        user = User.objects.filter(username=serializer.data['username'])
        Token.objects.create(user = user)
        return fun(*args)
    return wrapper


def get_token(user):
    return Token.objects.get(user=user)


# View for login
class LoginAPI(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        print(request.user)
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            return Response(status=200)
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)

# view for signup
class SignupAPI(CreateAPIView):
    serializer_class = SignupSerializer


class UpdateUserAPI(UpdateAPIView):
    serializer_class = User

# view for logout
def logoutView(request):
    logout(request)
    return Response({"logout":"succesfull"})


# view for handling file uploads

class FileListApiView(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = FileSerializer

    # get list of files
    def get(self, request, *args, **kwargs):
        queryset = File.objects.filter(username= request.user)
        print(queryset)
        serializer = FileSerializer(queryset, many=True)
        return Response(serializer.data)


class FileUploadAPIView(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = FileUploadSerializer
    # add a file

    def post(self,request):
        return self.create(request)


    def create(self, request):
        file_obj = File(filename = request.data.get('filename'),
                        file = request.FILES['file'].read(),
                        username = request.user)
        file_obj.save()
        return Response(status=200)


