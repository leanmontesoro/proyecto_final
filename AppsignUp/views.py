from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from AppsignUp.forms import RegistroUsuarioForm


def inicio(request):
    return render(request, "padre.html")


def register(request):
    if request.method=="POST":
        form=RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            clave=form.cleaned_data.get("password1")
            form.save()
            
            usuario=authenticate(username=username, password=clave)#trae un usuario de la base, que tenga ese usuario y ese pass, si existe, lo trae y si no None
            login(request, usuario)
            return render(request, "index.html", {"mensaje":f"Bienvenido {username} !"})
        else:
            return render(request, "signUp.html", {"form":form, "mensaje":"Error al crear el usuario"}) 
     
    else:
        form=RegistroUsuarioForm()
    return render(request, "signUp.html", {"form":form})