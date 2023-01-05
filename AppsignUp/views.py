from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from AppsignUp.forms import RegistroUsuarioForm
from AppMain.models import Avatar,Entrada
from AppProfile.views import obtenerAvatar

# def obtenerAvatar(request):
#     lista=Avatar.objects.filter(user=request.user)
#     if len(lista)!=0:
#         imagen=lista[0].imagen.url
#     else:
#         imagen="/media/avatarpordefecto3.png"
#     return imagen

# def inicio(request):
#     return render(request, "padre.html")

def register(request):
    if request.method=="POST":
        form=RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            clave=form.cleaned_data.get("password1")
            form.save()
            
            usuario=authenticate(username=username, password=clave)
            login(request, usuario)
            entradas=Entrada.objects.all()
            return render(request, "index.html", {"entradas":entradas,"mensaje":f"Bienvenido {username} !","avatar":obtenerAvatar(request)})
        else:
            return render(request, "signUp.html", {"form":form, "mensaje":"Error al crear el usuario"}) 
    
    else:
        form=RegistroUsuarioForm()
    return render(request, "signUp.html", {"form":form})