from django.shortcuts import render
from AppProfile.forms import UserEditForm
from AppMain.models import Avatar,Entrada
# Create your views here.


def obtenerAvatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen="/media/avatarpordefecto3.png"
    return imagen

#TODO: @login_required
def editarPerfil(request):
    usuario=request.user
    
    if request.method=="POST":
        form=UserEditForm(request.POST)
        entradas=Entrada.objects.all()
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.web=info["web"]
            #usuario.image=info["image"]
            usuario.save()
            return render(request, "index.html", {"entradas":entradas,"mensaje":"Perfil editado correctamente","titulo":"BloGastro","imagen":obtenerAvatar(request)})
        else:
            return render(request, "editProfile.html", {"form":form, "nombreusuario":usuario.username, "mensaje":"Error al editar el perfil"})
    else:
        form=UserEditForm(instance=usuario)
        return render(request, "editProfile.html", {"form":form,"nombreusuario":usuario.username,"imagen":obtenerAvatar(request)})

