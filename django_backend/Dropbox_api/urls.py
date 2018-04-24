from rest_framework.urls import url
from .views import LoginAPI, FileListApiView, logoutView,SignupAPI,FileUploadAPIView

urlpatterns = [
    url(r'signup',SignupAPI.as_view(), name='signup'),
    url(r'login',LoginAPI.as_view(), name='login'),
    url(r'files$', FileListApiView.as_view(), name='files'),
    url(r'files/upoload',FileUploadAPIView.as_view(), name='filelist'),
    url(r'logout',logoutView, name='logout'),
]


















