from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin #para vistas basadas en clases CLASS
from django.contrib.auth.decorators import login_required #para vistas basadas en funciones DEF 
from AppProfile.models import Avatar 

def obtenerAvatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen="/media/avatarpordefecto.png"
    return imagen


def inicio(request):

    lista=Avatar.objects.filter(user=request.user)
    
    return render (request, "index.html", {"imagen":obtenerAvatar(request)})
       #return render (request, "index.html")