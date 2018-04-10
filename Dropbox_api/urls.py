from rest_framework.urls import url
from .views import Signin, UserList, logoutView

urlpatterns = [
    url(r'login',Signin.as_view(), name='login'),
    url(r'userlist', UserList.as_view(), name='userlist'),
    url(r'logout',logoutView, name='logout'),
]


















