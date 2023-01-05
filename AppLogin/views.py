from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from AppMain.models import Avatar,Entrada
from AppProfile.views import obtenerAvatar


def login_req(request):
    if request.method == "POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu=form.cleaned_data.get("username")
            clave=form.cleaned_data.get("password")

            usuario=authenticate(username=usu, password=clave)#trae un usuario de la base, que tenga ese usuario y ese pass, si existe, lo trae y si no None

            if usuario is not None:    
                login(request, usuario)
                entradas=Entrada.objects.all()
                return render(request, 'index.html', {"entradas":entradas,'mensaje':f"Bienvenido {usuario}",'titulo':"BloGastro",'descripcion':"","avatar":obtenerAvatar(request)} )
            else:
                return render(request, 'login.html', {'mensaje':"Usuario o contraseña incorrectos", 'form':form})

        else:
            return render(request, 'login.html', {'mensaje':"Usuario o contraseña incorrectos", 'form':form})

    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form":form})    