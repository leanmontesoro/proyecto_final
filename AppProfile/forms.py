from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User


    
class UserEditForm(UserCreationForm):
    email = forms.EmailField()
    password1= forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)
    first_name=forms.CharField(label='Nombre')
    last_name=forms.CharField(label='Apellido')
    web=forms.URLField(label='Web',widget=forms.TextInput(attrs={'placeholder': 'https://www.example.com'}))
    image=forms.ImageField()

    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2', 'first_name', 'last_name','web','image']
        help_texts = {k:"" for k in fields} 


# class UserEditForm(UserCreationForm):
    
#     email = forms.EmailField()
#     password1= forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
#     password2= forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)
#     first_name=forms.CharField(label='Modificar Nombre')
#     last_name=forms.CharField(label='Modificar Apellido')

#     class Meta:
#         model = User
#         fields = [ 'email', 'password1', 'password2', 'first_name', 'last_name']
#         help_texts = {k:"" for k in fields} 

class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")