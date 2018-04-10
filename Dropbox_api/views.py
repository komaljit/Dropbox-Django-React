from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView, Http404, status
from .serializers import LoginSerializer, UserListSerializer
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class Signin(APIView):
    serializer_class = LoginSerializer
    # permission_classes = ['AllowAny',]
    # def post(self, request, *args, **kwargs):
    #     print(request.data)
    #     serializer = LoginSerializer(data=request.data)
    #     if serializer.is_valid():
    #         login(request, user=request.data['username'], password = request.data['password'])
    #         #login(request,user=serializer.validated_data)
    #         print(serializer.data)
    #
    #         return Response(request.data)
    #     else:
    #         return Response(request.data)


    def post(self, request, ):

        users = User.objects.all()
        # for user in users:
        #
        #     Token.objects.create(user=user)
        #     print(user.auth_token)
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request=request, username=username, password=password)

        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


class UserList(APIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

    def get(self, request, *args, **kwargs):
        queryset = User.objects.all()

        #serializer_class = UserListSerializer
        serializer = UserListSerializer(queryset, many=True)

        return Response(serializer.data)

@login_required
def logoutView(request):
    logout(request)
    return Response({"ff":"dd"})


























