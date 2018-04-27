from django.db import models
from django.contrib.auth.models import User


class File(models.Model):
    filename = models.CharField(max_length=50)
    file = models.FileField()
    username = models.ForeignKey(User, on_delete = models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)




