from django.shortcuts import render
from django.contrib.auth.decorators import login_required 
from AppMain.models import Avatar,Entrada
from AppMain.forms import AvatarForm,EntradaForm
from AppProfile.views import obtenerAvatar

   

def inicio(request):
    entradas=Entrada.objects.all()
    return render (request, "index.html",{"entradas":entradas,"titulo":"BloGastro","descripcion":"Un blog para el buen comer","avatar":obtenerAvatar(request)})
    


@login_required
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
            resume=informacion["resume"]
            read_time=informacion["read_time"]
            

            entrada= Entrada(titulo=titulo,subtitulo=subtitulo,cuerpo=cuerpo,autor=autor,fecha=fecha,resume=resume,read_time=read_time)
            entrada.save()
            entradas=Entrada.objects.all()
            return render (request, "index.html", {"entradas":entradas,"mensaje": "Entrada creada correctamente!", "avatar":obtenerAvatar(request)})
    else:

        #form=EntradaForm(initial={"autor":request.user})
        form=EntradaForm()
        return render (request, "addEntrada.html", {"form":form, "avatar":obtenerAvatar(request)})


def leerEntradas(request):
    entradas=Entrada.objects.all()
    
    return render(request, "leerEditEntrada.html", {"entradas":entradas,"titulo":"Entradas disponibles","avatar":obtenerAvatar(request)})


@login_required
def deleteEntradas(request, id):
    entrada=Entrada.objects.get(id=id)
    entrada.delete()
    entradas=Entrada.objects.all()
    
    return render(request, "deleteEntrada.html", {"entradas":entradas,"titulo":"Eliminar entradas","avatar":obtenerAvatar(request)})

@login_required
def detailEntrada(request,id):
    entrada=Entrada.objects.get(id=id)
    
    return render(request, "detailEntrada.html", {"entrada":entrada,"titulo":"BloGastro","avatar":obtenerAvatar(request)}) 

@login_required
def homeDeleteEntradas(request):
    
    if request.user.is_superuser > 0:
        entradas=Entrada.objects.all()
    else:
        entradas=Entrada.objects.filter(autor=request.user)

    return render(request, "deleteEntrada.html", {"entradas":entradas,"titulo":"Eliminar entradas","avatar":obtenerAvatar(request)})

@login_required
def homeEditEntradas(request):
    
    if request.user.is_superuser > 0:
        entradas=Entrada.objects.all()
    else:
        entradas=Entrada.objects.filter(autor=request.user)

    return render(request, "leerEditEntrada.html", {"entradas":entradas,"titulo":"Editar entradas","avatar":obtenerAvatar(request)})




@login_required
def editEntrada(request,id):
    entrada=Entrada.objects.get(id=id)
    

    if request.method=="POST":
        form=EntradaForm(request.POST)

        if form.is_valid():
            
            info=form.cleaned_data
            entrada.titulo=info["titulo"]
            entrada.subtitulo=info["subtitulo"]
            entrada.cuerpo=info["cuerpo"]
            entrada.resume=info["resume"]
            entrada.read_time=info["read_time"]
            entrada.autor=info["autor"]
            entrada.fecha=info["fecha"]
            
            entrada.save()
            entradas=Entrada.objects.all()
            return render(request, "index.html", {"entradas":entradas,"mensaje":"Entrada editado correctamente","titulo":"BloGastro","avatar":obtenerAvatar(request)})
        else:
            
            return render(request, "editEntrada.html", {"form":form, "mensaje":"Error al editar la entrada"})
    else:
        
        form=EntradaForm(initial={"titulo":entrada.titulo,"subtitulo":entrada.subtitulo,"cuerpo":entrada.cuerpo,"resume":entrada.resume,"read_time":entrada.read_time,"autor":entrada.autor,
        "fecha":entrada.fecha})

        
        return render(request, "editEntrada.html", {"form":form,"avatar":obtenerAvatar(request),"entrada":entrada})

@login_required
def about(request):
      
    return render(request, "about.html",{"avatar":obtenerAvatar(request)})     

@login_required
def enviarMensaje(request):

    if request.method=="POST":
        form=MensajeForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data

            emisor=informacion["emisor"]
            receptor=informacion["receptor"]
            cuerpo=informacion["cuerpo"]
            #leido=informacion["leido"]
                       

            mensaje= Mensaje(emisor=emisor,receptor=receptor,cuerpo=cuerpo,leido=False)
            mensaje.save()
            entradas=Entrada.objects.all()
            return render (request, "index.html", {"entradas":entradas,"mensaje": "Mensaje enviado correctamente!", "avatar":obtenerAvatar(request)})
    else:

        form=MensajeForm(initial={"emisor":request.user})
        return render (request, "enviarMensaje.html", {"form":form, "avatar":obtenerAvatar(request)})    
    
@login_required
def leerMensajes(request):

    mensajes=Mensaje.objects.filter(receptor__icontains=request.user)

    if len(mensajes)!=0:
        msj=mensajes[0].receptor
        return render (request, "leerMensaje.html", {"form":mensajes, "avatar":obtenerAvatar(request)})      
        
    else:
        msj="/media/avatares/avatarpordefecto.png"
        print(msj)
   

    #return render (request, "leerMensaje.html", {"form":mensajes, "imagen":obtenerAvatar(request)}) 
