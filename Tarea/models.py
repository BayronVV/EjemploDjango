from django.db import models
from django.utils import timezone


# Create your models here.

class Pendiente(models.Model):

    name = models.CharField(max_length=50)
    descripcion=models.TextField(max_length=200)
    priority=models.IntegerField(default=1)
    created_at=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
