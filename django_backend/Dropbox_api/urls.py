from rest_framework.urls import url
from .views import (LoginAPI, FileListApiView,
                    logoutView, SignupAPI, DeleteApiView,
                    FileUploadAPIView, UpdateUserAPI,
                        )
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'signup',SignupAPI.as_view(), name='signup'),
    url(r'update',UpdateUserAPI.as_view(), name='update_user'),
    url(r'delete',DeleteApiView.as_view(), name='delete'),
    url(r'login',LoginAPI.as_view(), name='login'),
    url(r'files$', FileListApiView.as_view(), name='files'),
    url(r'file/upload',FileUploadAPIView.as_view(), name='filelist'),
    url(r'logout',logoutView.as_view(), name='logout'),
]



