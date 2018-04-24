from rest_framework.urls import url
from .views import LoginAPI, UserListAPI, logoutView,SignupAPI,FileApiView

urlpatterns = [
    url(r'signup',SignupAPI.as_view(), name='signup'),
    url(r'login',LoginAPI.as_view(), name='login'),
    url(r'userlist', UserListAPI.as_view(), name='userlist'),
    url(r'addfile',FileApiView.as_view(), name='filelist'),
    url(r'logout',logoutView, name='logout'),
]


















