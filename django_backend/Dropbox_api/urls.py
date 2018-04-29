from rest_framework.urls import url
from .views import (LoginAPI, FileListApiView,
                    LogoutView, SignupAPI, DeleteUserApiView, DeleteFileApiview,
                    FileUploadAPIView, UpdateUserAPI, UserDetailsView
                    )

urlpatterns = [
    url(r'^signup',SignupAPI.as_view(), name='signup'),
    url(r'^update',UpdateUserAPI.as_view(), name='update_user'),
    url(r'^details', UserDetailsView.as_view(), name='userdetails'),
    url(r'^delete',DeleteUserApiView.as_view(), name='delete'),
    url(r'^login',LoginAPI.as_view(), name='login'),
    url(r'^files/$', FileListApiView.as_view(), name='files'),
    url(r'^file/upload/$',FileUploadAPIView.as_view(), name='filelist'),
    url(r'^file/?(?P<pk>\d+)/$',DeleteFileApiview.as_view(), name='download_file'),
    url(r'^file/delete/?(?P<pk>\d+)/$',DeleteFileApiview.as_view(), name='deletefile'),
    url(r'^logout',LogoutView.as_view(), name='logout'),
]

