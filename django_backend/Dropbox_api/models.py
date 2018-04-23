from django.db import models


class File(models.Model):
    filename = models.CharField(max_length=50)
    file = models.FileField()
    # user_id = models.ForeignKey('User.id', on_delete = models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
