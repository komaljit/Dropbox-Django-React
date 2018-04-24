from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.views import APIView, status
from .serializers import LoginSerializer, UserListSerializer, SignupSerializer, FileSerializer
from .models import File
from rest_framework.response import Response
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


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
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        request.session['user'] = username
        if user:
            login(request,user)
            return Response(status=200)
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


# view for signup
class SignupAPI(CreateAPIView):
    serializer_class = SignupSerializer


# view for logout
@login_required
def logoutView(request):
    logout(request)
    return Response({"logout":"succesfull"})


# view for handling file uploads
@login_required
class FileListApiView(APIView):
    serializer_class = FileSerializer

    # get list of files
    def get(self, request, *args, **kwargs):
        queryset = File.objects.filter(username= request.session['user'])
        serializer = FileSerializer(queryset, many=True)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(status=404)

@login_required
class FileUploadAPIView(APIView):
    serializer_class = FileSerializer
    # add a file
    def post(self,request):
        if not request.session['user']:
            return Response({"login required"})
        serializer = FileSerializer(data = request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=200)
        return Response(status=404)




