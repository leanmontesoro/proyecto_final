from django import forms
from django.db import models
from django.contrib.auth.models import User




class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")


class EntradaForm(forms.Form):
    titulo=forms.CharField(max_length=50)
    subtitulo=forms.CharField(max_length=50)
    cuerpo=forms.CharField(max_length=5000)
    resume=forms.CharField(max_length=50)
    read_time=forms.CharField(max_length=50)
    autor=forms.CharField(max_length=50)
    fecha=forms.DateField()
    #imagen=forms.ImageField()