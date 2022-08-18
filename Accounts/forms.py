from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class RegisterForm(forms.Form):
    Nombre_de_usuario = forms.CharField(max_length=30)
    Contraseña = forms.PasswordInput()
    Email = forms.EmailField(max_length = 150)

    Nombre = forms.CharField(max_length = 50)
    Apellido = forms.CharField(max_length = 50)
    Imagen = forms.ImageField()
    Descripcion = forms.CharField(widget = forms.Textarea, max_length = 2000)

    