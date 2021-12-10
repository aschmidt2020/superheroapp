from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from villains.models import Villain
from superheroes.models import Superhero

# Create your views here.
def index(request):
    all_heroes = Superhero.objects.all()
    context = {'all_heroes': all_heroes}
    return render(request, 'superheroes/index.html', context)

def detail(request, hero_id):
    single_hero = Superhero.objects.get(pk=hero_id)
    context = {'single_hero': single_hero}
    return render (request, 'superheroes/detail.html', context)

def create(request):
    if request.method == "POST":
        #save the form contents as a new db object by instantiating new hero
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary_ability = request.POST.get('primary_ability')
        secondary_ability = request.POST.get('secondary_ability')
        catchphrase = request.POST.get('catchphrase')
        villain_name = request.POST.get('villain')
        villain = Villain.objects.get(name=villain_name)
        
        new_hero = Superhero(name=name, alter_ego=alter_ego, primary_ability=primary_ability, secondary_ability=secondary_ability, 
                             catchphrase=catchphrase, villain=villain)
        new_hero.save()
        
        #return to index.html
        return HttpResponseRedirect(reverse('superheroes:index'))
        
    else:
        return render(request, 'superheroes/create.html')

def delete(request, hero_id):
    if request.method == "POST":
        single_hero = Superhero.objects.get(pk=hero_id)
        single_hero.delete()
    
        return HttpResponseRedirect(reverse('superheroes:index'))
    
    else:
        single_hero = Superhero.objects.get(pk=hero_id)
        context = {'single_hero': single_hero}
        return render (request, 'superheroes/delete.html', context)

def update(request, hero_id):
    if request.method == "POST":
        single_hero = Superhero.objects.get(pk=hero_id)
        
        single_hero.name = request.POST.get('name')
        single_hero.alter_ego = request.POST.get('alter_ego')
        single_hero.primary_ability = request.POST.get('primary_ability')
        single_hero.secondary_ability = request.POST.get('secondary_ability')
        single_hero.catchphrase = request.POST.get('catchphrase')
        villain_name = request.POST.get('villain')
        single_hero.villain = Villain.objects.get(name=villain_name)

        single_hero.save()
        
        return HttpResponseRedirect(reverse('superheroes:index'))
    
    else:
        single_hero = Superhero.objects.get(pk=hero_id)
        context = {'single_hero': single_hero}
        return render (request, 'superheroes/update.html', context)
        