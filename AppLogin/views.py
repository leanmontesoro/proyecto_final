from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from AppMain.models import Avatar



def obtenerAvatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen="/media/avatarpordefecto3.png"
    return imagen

def login_req(request):
    if request.method == "POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu=form.cleaned_data.get("username")
            clave=form.cleaned_data.get("password")

            usuario=authenticate(username=usu, password=clave)#trae un usuario de la base, que tenga ese usuario y ese pass, si existe, lo trae y si no None

            if usuario is not None:    
                login(request, usuario)
                return render(request, 'index.html', {'mensaje':f"Bienvenido {usuario}",'titulo':"CookAlgo",'descripcion':"","imagen":obtenerAvatar(request)} )
            else:
                return render(request, 'login.html', {'mensaje':"Usuario o contraseña incorrectos", 'form':form})

        else:
            return render(request, 'login.html', {'mensaje':"Usuario o contraseña incorrectos", 'form':form})

    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form":form})    