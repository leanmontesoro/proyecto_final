from django.urls import path, include
from . import views
from django.contrib import admin
from django.urls import path
from AppMensajeria.views import *
# se importa el logout directamente al url
from django.contrib.auth.views import LogoutView
urlpatterns = [
    
    path("formMensajes", formMensajes , name = "formMensajes"),
    path("homeMensajes", homeMensajes , name = "homeMensajes"),
    path("inboxMensajes", inboxMensajes , name = "inboxMensajes"),
    path("outboxMensajes", outboxMensajes , name = "outboxMensajes"),
    
]