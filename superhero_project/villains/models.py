from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Villain(models.Model):
    name = models.CharField(max_length=50)
    superpower = models.CharField(max_length=50, default=None)
    
    def __str__(self):
        return self.name
