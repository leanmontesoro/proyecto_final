from django.urls import path
from AppMain.views import inicio
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
]