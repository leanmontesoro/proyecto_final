from django import forms
from django.contrib.auth.models import User


class MensajeForm(forms.Form):
    receiver = forms.ModelChoiceField(User.objects.all(),label="Seleccione al receptor")
    mensaje = forms.CharField(max_length=8000)