from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import  UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from AppProfile.models import Perfil


    
class UserEditForm(UserChangeForm):
    #username = forms.CharField()
    email = forms.EmailField()
    #password1= forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    #password2= forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)
    first_name=forms.CharField(label='Nombre')
    last_name=forms.CharField(label='Apellido')
    
    class Meta:
        model = User
        fields = [ 'email', 'first_name', 'last_name']
        help_texts = {k:"" for k in fields} 


class Perfil_Form(ModelForm):
    class Meta:
        model = Perfil
        fields = ['descripcion', 'web', 'avatar']


class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")