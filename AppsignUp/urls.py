from django.urls import path
from AppsignUp.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", inicio, name="inicio"),
    path("signup/", register, name="register"), #url navegador + vista + id para jinja
   
]