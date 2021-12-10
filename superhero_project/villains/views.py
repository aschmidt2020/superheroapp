from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from villains.models import Villain

# Create your views here.
def create(request):
    if request.method == "POST":
        #save the form contents as a new db object by instantiating new hero
        name = request.POST.get('name')
        superpower = request.POST.get('superpower')
        
        new_villain = Villain(name=name, superpower=superpower)
        new_villain.save()
        
        #return to index.html
        return HttpResponseRedirect(reverse('superheroes:index'))
        
    else:
        return render(request, 'villains/create.html')

def detail(request, villain_id):
    single_villain = Villain.objects.get(pk=villain_id)
    context = {'single_villain': single_villain}
    return render (request, 'villains/detail.html', context)