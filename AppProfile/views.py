from django.shortcuts import render
from AppProfile.forms import Perfil_Form, UserEditForm
from django.contrib.auth import update_session_auth_hash
from AppMain.models import Avatar,Entrada
from AppProfile.models import Perfil
from django.contrib.auth.models import User
from django.contrib.auth.forms import  PasswordChangeForm
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
        user_actual = User.objects.get(username = request.user)

        if edit_form.is_valid():
            informacion=edit_form.cleaned_data

            user_actual.email=informacion["email"]
            user_actual.first_name=informacion["first_name"]
            user_actual.last_name=informacion["last_name"]
            user_actual.save()

            return render(request, "index.html", {"mensaje": f"El usuario {request.user} ha sido editado exitosamente!", "avatar": obtenerAvatar(request)})

        else:
            
            return render(request, "editUser.html", {"form" : UserEditForm(instance = request.user), "mensaje": "Intentelo Nuevamente, hubo un error", "avatar": obtenerAvatar(request)}) 

    else:
        
        edit_form = UserEditForm(instance = request.user)
        return render(request, "editUser.html", {"form":edit_form, "mensaje":"Editar perfil", "avatar": obtenerAvatar(request)})


def editPassword(request):
    entradas=Entrada.objects.all()
    if request.method == "POST":
        form = PasswordChangeForm(data = request.POST, user = request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return render(request, "index.html", {"mensaje": "La contraseña ha sido editada exitosamente!","entradas":entradas, "avatar": obtenerAvatar(request)})
        else:
           return render(request, "editPassword.html", {"form" : PasswordChangeForm(user = request.user),"entradas":entradas, "mensaje": "Ocurrió un error, intentelo nuevamente", "avatar": obtenerAvatar(request)})
    else:
        return render(request, "editPassword.html", {"form": PasswordChangeForm(user = request.user),"entradas":entradas, "avatar": obtenerAvatar(request)})
       
