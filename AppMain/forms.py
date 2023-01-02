from django import forms
from django.db import models
from django.contrib.auth.models import User
from AppMain.models import Entrada
from ckeditor_uploader.fields import RichTextUploadingField 




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
    imagen=forms.ImageField()
    body=RichTextUploadingField()
    

    class Meta:
        model = Entrada
        fields = [ 'titulo', 'subtitulo', 'cuerpo', 'resume', 'read_time','autor','fecha','imagen','body']
        #help_texts = {k:"" for k in fields}         