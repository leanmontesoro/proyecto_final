from django.shortcuts import render
from django.contrib.auth.models import User
from AppMensajeria.models import *
from AppMensajeria import *
from django.contrib.auth.decorators import login_required
from AppProfile.views import obtenerAvatar
from AppMensajeria.forms import MensajeForm


# Create your views here.
@login_required
def homeMensajes(request):
    return render(request, 'homeMensajes.html',{'users': User.objects.exclude(username=request.user.username), "avatar": obtenerAvatar(request)})


@login_required
def formMensajes(request):
    usuario=request.user 
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():

            informacion = form.cleaned_data
            print(informacion)

            receptor = informacion['receiver']
            mensaje = informacion['mensaje']
            mensajeNuevo = Mensaje(enviar=(usuario), recibir = (receptor), mensaje=mensaje, leido = False)
            mensajeNuevo.save()

            formulario = MensajeForm()
            return render(request, 'homeMensajes.html', {"form": formulario, "mensaje": "El mensaje ha sido enviado exitosamente!", "avatar": obtenerAvatar(request)} )
        else:
            return render(request, 'homeMensajes.html', {"mensaje": "Hubo un error, intentelo nuevamente", "avatar": obtenerAvatar(request)} )
    else:
        formulario = MensajeForm()
        return render(request, 'formMensajes.html', {"form": formulario, "avatar": obtenerAvatar(request)} )

def inboxMensajes(request):
    usuario = request.user
    print(usuario.id)
    inbox = Mensaje.objects.filter(recibir_id = usuario.id)
    print(inbox)
    for mensaje in inbox:
        mensaje.leido = True
        mensaje.save()  
    return render(request, "inboxMensajes.html", {"mensajes": inbox, "avatar": obtenerAvatar(request)})


@login_required
def outboxMensajes(request):
    usuario = request.user
    outbox = Mensaje.objects.filter(enviar = usuario)
    return render(request, "outboxMensajes.html", {"mensajes": outbox, "avatar": obtenerAvatar(request)})