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
    return render (request, "index.html",{"entradas":entradas,"titulo":"BloGastro","descripcion":"Un blog para el buen comer",})
    
    


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

        form=EntradaForm(initial={entrada.autor:request.user})
        return render (request, "addEntrada.html", {"form":form, "imagen":obtenerAvatar(request)})


def leerEntradas(request):
    entradas=Entrada.objects.all()
    #print(entradas)
    return render(request, "leerEditEntrada.html", {"entradas":entradas,"titulo":"Entradas disponibles","imagen":obtenerAvatar(request)})



def deleteEntradas(request, id):
    entrada=Entrada.objects.get(id=id)
    entrada.delete()
    entradas=Entrada.objects.all()
    
    return render(request, "deleteEntrada.html", {"entradas":entradas,"titulo":"Eliminar entradas","imagen":obtenerAvatar(request)})

def detailEntrada(request,id):
    entrada=Entrada.objects.get(id=id)
    
    return render(request, "detailEntrada.html", {"entrada":entrada,"titulo":"Blog","imagen":obtenerAvatar(request)}) 


def homeDeleteEntradas(request):
    
    if request.user.is_superuser > 0:
        entradas=Entrada.objects.all()
    else:
        entradas=Entrada.objects.filter(autor=request.user)

    return render(request, "deleteEntrada.html", {"entradas":entradas,"titulo":"Eliminar entradas","imagen":obtenerAvatar(request)})


def homeEditEntradas(request):
    
    if request.user.is_superuser > 0:
        entradas=Entrada.objects.all()
    else:
        entradas=Entrada.objects.filter(autor=request.user)

    return render(request, "leerEditEntrada.html", {"entradas":entradas,"titulo":"Editar entradas","imagen":obtenerAvatar(request)})




#TODO: @login_required
def editEntrada(request,id):
    entrada=Entrada.objects.get(id=id)
    
    if request.method=="POST":
        form=EntradaForm(request.POST)
        #print(request.POST)
        print(EntradaForm())
        print(form)
        print("estoy en el post")
        if form.is_valid():
            print("estoy en el post y soy valido")
            info=form.cleaned_data
            entrada.titulo=info["titulo"]
            entrada.subtitulo=info["subtitulo"]
            entrada.cuerpo=info["cuerpo"]
            entrada.resume=info["resume"]
            entrada.read_time=info["read_time"]
            entrada.autor=info["autor"]
            entrada.fecha=info["fecha"]
            #entrada.imagen=info["imagen"]
            entrada.save()
            entradas=Entrada.objects.all()
            return render(request, "index.html", {"entradas":entradas,"mensaje":"Entrada editado correctamente","titulo":"BloGastro","imagen":obtenerAvatar(request)})
        else:
            print("estoy en el post y no soy valido")
            return render(request, "editEntrada.html", {"form":form, "mensaje":"Error al editar la entrada"})
    else:
        
        form=EntradaForm(initial={"titulo":entrada.titulo,"subtitulo":entrada.subtitulo,"cuerpo":entrada.cuerpo,"resume":entrada.resume,"read_time":entrada.read_time,"autor":entrada.autor,
        "fecha":entrada.fecha})
        print("estoy en el get")
        
        return render(request, "editEntrada.html", {"form":form,"imagen":obtenerAvatar(request),"entrada":entrada})


def about(request):
    #entrada=Entrada.objects.get(id=id)
    
    return render(request, "about.html",{"imagen":obtenerAvatar(request)})     
