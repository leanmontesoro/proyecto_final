from django.urls import path
from AppMain.views import inicio
from AppLogin.views import *
from AppsignUp.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path("", inicio, name="inicio"),
    path("signup/", register, name="register"),

]