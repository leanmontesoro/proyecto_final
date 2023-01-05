from django.shortcuts import render
from AppProfile.forms import Perfil_Form, UserEditForm
from AppMain.models import Avatar,Entrada
from AppProfile.models import Perfil
from django.contrib.auth.models import User
# Create your views here.


def obtenerAvatar(request):

    if request.user.is_authenticated:
        lista=Perfil.objects.filter(user=request.user)
        if len(lista)!=0:
            imagen=lista[0].avatar.url
        else:
            imagen="/media/avatarpordefecto3.png"
        
    else: imagen = ""

    return imagen


def editarPerfil(request):
    datos_actuales = Perfil.objects.filter(user = request.user)
    print("Entre")
    if datos_actuales:
        print("Entre_datos actuales true")
        formulario_edit = Perfil_Form(initial={"descripcion": datos_actuales[0].descripcion, "web": datos_actuales[0].web, "avatar": datos_actuales[0].avatar})
    else:
        formulario_edit = Perfil_Form()
        print("Entre_datos actuales false")
    
    if request.method == "POST":
        formulario = Perfil_Form(request.POST, request.FILES)
        
        
        if formulario.is_valid():
            
            datos_actuales = Perfil.objects.filter(user = request.user)
            if datos_actuales != None:
                        
                datos_actuales.delete()
                datos_nuevos = Perfil(user=request.user, descripcion = request.POST["descripcion"], web = request.POST["web"], avatar = request.FILES["avatar"] )
                datos_nuevos.save()
                return render(request, "index.html", {"mensaje": "Perfil editado exitosamente!", "avatar": obtenerAvatar(request)})
        else:
            return render(request, "editProfile.html", {"form" : formulario_edit, "mensaje": "Error al editar el perfil", "avatar": obtenerAvatar(request)})
    else:
        print("soyget")
        return render(request, "editProfile.html", {"form": formulario_edit, "mensaje":"Editar perfil","nombreusuario":request.user, "avatar": obtenerAvatar(request)}) 



def editarUsuario(request):
    if request.method == "POST":
        edit_form = UserEditForm(request.POST)
        user_viejos = User.objects.filter(username = request.user)
        print(user_viejos)
        print("soy post")
        if edit_form.is_valid():
            print("soy valido")
            print(edit_form)
            edit_form.save()
            return render(request, "index.html", {"mensaje": f"El usuario {request.user} ha sido editado exitosamente!", "imagen": obtenerAvatar(request)})

        else:
            print("soy no soy valido")
            return render(request, "editUser.html", {"form" : UserEditForm(instance = request.user), "mensaje_registro": "Intentelo Nuevamente, hubo un error", "avatar": obtenerAvatar(request)}) 

    else:
        print("soy GET")
        edit_form = UserEditForm(instance = request.user)
        return render(request, "editUser.html", {"form":edit_form, "mensaje":"Editar perfil", "avatar": obtenerAvatar(request)})
        
