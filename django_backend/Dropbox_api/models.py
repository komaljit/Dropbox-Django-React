from django.db import models


class File(models.Model):
    filename = models.CharField()
    username = models.CharField()
