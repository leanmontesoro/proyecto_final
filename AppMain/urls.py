from django.urls import path
from AppMain.views import inicio,addEntrada,leerEntradas,deleteEntradas,homeDeleteEntradas,detailEntrada,about,editEntrada,homeEditEntradas
from AppLogin.views import login_req
from AppProfile.views import editPassword
from AppsignUp.views import register
from AppProfile.views import editarPerfil, editarUsuario
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path("", inicio, name="inicio"),
    path("signup/", register, name="register"),
    path("login/", login_req,name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("editPassword/", editPassword,name="editPassword"),
    
    
    path("agregarEntrada/", addEntrada, name="agregarEntrada"),
    path("detailEntrada/<id>", detailEntrada, name="detailEntrada"),
    path("homeDeleteEntradas/", homeDeleteEntradas, name="homeDeleteEntradas"),
    path("deleteEntradas/<id>", deleteEntradas, name="deleteEntradas"),
    path("homeEditEntradas/", homeEditEntradas, name="homeEditEntradas"),
    path("editEntrada/<id>", editEntrada, name="editEntrada"),
    path("leerEntradas/", leerEntradas, name="leerEntradas"), 
    

    path("editUser/", editarUsuario, name="editUser"),
    path("editProfile/", editarPerfil, name="editProfile"),
    path("about/", about, name="about")

]