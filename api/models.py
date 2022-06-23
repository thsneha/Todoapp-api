from django.db import models

# Create your models here.
class Todos(models.Model):
    taskname=models.CharField(max_length=123)
    user=models.CharField(max_length=120)
    status=models.BooleanField(default=False)#complete status.starting time status is false

    def __str__(self):
        return self.taskname