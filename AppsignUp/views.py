from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from AppsignUp.forms import RegistroUsuarioForm


# def registrar(request):
        
#     return render (request, "signUp.html")


def register(request):
    if request.method=="POST":
        form=RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            form.save()
            #aca se podria loguear el usuario, con authenticate y login... pero no lo hago
            return render(request, "../AppMain/padre.html", {"mensaje":f"Usuario {username} creado correctamente"})
        else:
            return render(request, "index.html", {"form":form, "mensaje":"Error al crear el usuario"})
     
    else:
        form=RegistroUsuarioForm()
    return render(request, "signUp.html", {"form":form})