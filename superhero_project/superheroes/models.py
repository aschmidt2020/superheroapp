from django.db import models
from django.db.models.fields import CharField

from villains.models import Villain




# Create your models here.
class Superhero(models.Model):
    name = models.CharField(max_length=50)
    alter_ego = models.CharField(max_length=50)
    primary_ability = models.CharField(max_length=50)
    secondary_ability = models.CharField(max_length=50)
    catchphrase = models.CharField(max_length=50)
    villain = models.ForeignKey(Villain, default=None, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name