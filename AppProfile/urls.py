from django.urls import path
from AppProfile.views import editarPerfil

urlpatterns = [
    path("editProfile/", editarPerfil, name="editProfile"),
    path("editPassword/", editarPerfil, name="editPassword"),
    
   
]