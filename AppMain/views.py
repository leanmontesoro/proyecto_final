from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin #para vistas basadas en clases CLASS
from django.contrib.auth.decorators import login_required #para vistas basadas en funciones DEF 
from AppMain.models import Avatar,Entrada
from AppMain.forms import AvatarForm,EntradaForm



def obtenerAvatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen="/media/avatarpordefecto3.png"
    return imagen
    

def inicio(request):
    entradas=Entrada.objects.all()
    return render (request, "index.html",{"entradas":entradas,"titulo":"Blog title index","descripcion":"descripción en index"})
    #return render (request, "index.html", {"imagen":obtenerAvatar(request)})
    


@login_required
def agregarAvatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatarViejo=Avatar.objects.filter(user=request.user)
            if len(avatarViejo)!=0:
                avatarViejo[0].delete()
            avatar=Avatar(user=request.user, imagen=request.FILES["imagen"])
            avatar.save()
            return render(request, "index.html", {"mensaje":"Avatar agregado correctamente","imagen":obtenerAvatar(request)})
        else:
            return render(request, "addAvatar.html", {"form": form, "usuario": request.user})
    else:
        form=AvatarForm()
        return render(request , "addAvatar.html", {"form": form, "usuario": request.user,"imagen":obtenerAvatar(request)})


def addEntrada(request):

    if request.method=="POST":
        form=EntradaForm(request.POST, request.FILES)
        if form.is_valid():
            informacion=form.cleaned_data

            titulo=informacion["titulo"]
            subtitulo=informacion["subtitulo"]
            cuerpo=informacion["cuerpo"]
            autor=informacion["autor"]
            fecha=informacion["fecha"]
            imagen=informacion["imagen"]

            entrada= Entrada(titulo=titulo,subtitulo=subtitulo,cuerpo=cuerpo,autor=autor,fecha=fecha,imagen=imagen)
            entrada.save()
            entradas=Entrada.objects.all()
            return render (request, "index.html", {"entradas":entradas,"mensaje": "Entrada creada correctamente!", "imagen":obtenerAvatar(request)})
    else:

        form=EntradaForm()
        return render (request, "addEntrada.html", {"form":form, "imagen":obtenerAvatar(request)})


def leerEntradas(request):
    entradas=Entrada.objects.all()
    #print(entradas)
    return render(request, "index.html", {"entradas":entradas,"titulo":"Entradas disponibles","imagen":obtenerAvatar(request)})

def homeDeleteEntradas(request):
    entradas=Entrada.objects.all()
    return render(request, "deleteEntrada.html", {"entradas":entradas,"titulo":"Eliminar entradas","imagen":obtenerAvatar(request)})

def deleteEntradas(request, id):
    entrada=Entrada.objects.get(id=id)
    entrada.delete()
    entradas=Entrada.objects.all()
    
    return render(request, "deleteEntrada.html", {"entradas":entradas,"titulo":"Eliminar entradas","imagen":obtenerAvatar(request)})
