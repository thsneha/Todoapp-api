from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todos(models.Model):
    taskname=models.CharField(max_length=123)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.BooleanField(default=False)#complete status.starting time status is false

    def __str__(self):
        return self.taskname