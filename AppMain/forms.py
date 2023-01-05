from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from AppMain.models import Entrada




class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")


class EntradaForm(ModelForm):
        
    class Meta:
        model = Entrada
        fields = ['titulo', 'subtitulo', 'cuerpo','resume','read_time','autor','fecha', 'imagen']



class MensajeForm(forms.Form):
    emisor=forms.CharField(max_length=50)
    receptor=forms.CharField(max_length=50)
    cuerpo=forms.CharField(max_length=5000)
    #leido=forms.BooleanField()