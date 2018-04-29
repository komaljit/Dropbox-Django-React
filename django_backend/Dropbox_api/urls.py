from rest_framework.urls import url
from .views import (LoginAPI, FileListApiView,
                    LogoutView, SignupAPI, DeleteApiView,
                    FileUploadAPIView, UpdateUserAPI, UserDetailsView
                        )
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'signup',SignupAPI.as_view(), name='signup'),
    url(r'update',UpdateUserAPI.as_view(), name='update_user'),
    url(r'details', UserDetailsView.as_view(), name='userdetails'),
    url(r'delete',DeleteApiView.as_view(), name='delete'),
    url(r'login',LoginAPI.as_view(), name='login'),
    url(r'files$', FileListApiView.as_view(), name='files'),
    url(r'file/upload',FileUploadAPIView.as_view(), name='filelist'),
    url(r'logout',LogoutView.as_view(), name='logout'),
]



