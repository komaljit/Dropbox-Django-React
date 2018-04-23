from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.views import APIView, Http404, status
from .serializers import LoginSerializer, UserListSerializer, SignupSerializer, FileSerializer
from .models import File
from rest_framework.response import Response
from django.contrib.auth import logout, authenticate
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

python

# View for login
class SigninAPI(APIView):
    serializer_class = LoginSerializer

    def post(self, request, ):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request=request, username=username, password=password)

        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)



# view for signup
class SignupAPI(CreateAPIView):
    serializer_class = SignupSerializer

    @generate_token
    def perform_create(self, serializer):
        serializer.save()



# view for obatinig userlist
class UserListAPI(APIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

    def get(self, request, *args, **kwargs):
        queryset = User.objects.all()
        serializer = UserListSerializer(queryset, many=True)
        return Response(serializer.data)



# view for logout
@login_required
def logoutView(request):
    logout(request)
    return Response({"logout":"succesfull"})

class FileApiView(APIView):

    def get(self, request, *args, **kwargs):
        queryset = File.objects.filter(username='session')
        serializer = FileSerializer(queryset, many=True)
        return Response(serializer.data)






























