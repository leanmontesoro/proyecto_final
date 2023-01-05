from django.db import models
from django.conf import settings
from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
#user = settings.AUTH_USER_MODEL

class Mensaje(models.Model):
    enviar = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    recibir = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    mensaje = models.TextField(max_length=8000)
    hora = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)

    def __str__(self):
        return  str(self.leido) + " "+ self.mensaje + " "+ str(self.hora)