from django.db import models
from django.contrib.auth.models import User


# File model for the class
class File(models.Model):
    filename = models.CharField(max_length=50)
    file = models.FileField()
    username = models.ForeignKey(User, on_delete = models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


class folder(models.Model):
    foldername = models.ForeignKey(User, on_delete=models.CASCADE)


class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length= 100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class group_member(models.Model):
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = User.username
