from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField 
# Create your models here.

class Avatar(models.Model):
    imagen=models.ImageField(upload_to='avatares')
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.imagen}"

class Entrada(models.Model):
    titulo=models.CharField(max_length=50)
    subtitulo=models.CharField(max_length=50)
    resume=models.CharField(max_length=50,default="resumen")
    read_time=models.CharField(max_length=50,default="No especificado")
    cuerpo= RichTextUploadingField() # CKEditor Rich Text Field
    autor=models.CharField(max_length=50)
    fecha=models.DateField()
    imagen=models.ImageField(upload_to='media', blank=True) #avatares?
    
    def __str__(self):
        return self.titulo+" "+self.subtitulo

