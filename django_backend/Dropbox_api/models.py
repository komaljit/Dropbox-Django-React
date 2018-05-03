from django.db import models
from django.contrib.auth.models import User


# Folder model for virtual folders
class Folder(models.Model):
    folder_path = models.CharField(max_length=300, primary_key=True)
    # foldername = models.CharField(max_length=20)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_folder = models.CharField(max_length=300, default=username)


# File model for the class
class File(models.Model):
    file_id = models.AutoField(primary_key=True)
    filename = models.CharField(max_length=50)
    file = models.FileField()
    folder_path = models.ForeignKey(Folder, on_delete = models.CASCADE)
    username = models.ForeignKey(User, on_delete = models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


# model for shared file groups
class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length= 100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class group_member(models.Model):
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = User.username