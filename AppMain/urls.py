from django.urls import path
from AppMain.views import inicio,agregarAvatar,addEntrada,leerEntradas,deleteEntradas,homeDeleteEntradas,detailEntrada,about
from AppLogin.views import login_req
from AppsignUp.views import register
from AppProfile.views import editarPerfil
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path("", inicio, name="inicio"),
    path("signup/", register, name="register"),
    path("login/", login_req,name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("editProfile/", editarPerfil, name="editProfile"),
    path("agregarAvatar/", agregarAvatar, name="agregarAvatar"),
    path("agregarEntrada/", addEntrada, name="agregarEntrada"),
    path("leerEntradas/", leerEntradas, name="leerEntradas"),
    path("detailEntrada/<id>", detailEntrada, name="detailEntrada"),
    path("homeDeleteEntradas/", homeDeleteEntradas, name="homeDeleteEntradas"),
    path("deleteEntradas/<id>", deleteEntradas, name="deleteEntradas"),
    path("about/", about, name="about")
]