from django.contrib import admin

from villains.models import Villain
from superheroes.models import Superhero

# Register your models here.
admin.site.register(Superhero)
admin.site.register(Villain)
