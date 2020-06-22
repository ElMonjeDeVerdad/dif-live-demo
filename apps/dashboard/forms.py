from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django import forms
from .models import Perfil

#Formulario para registar usuarios
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

#Asignar Empresa
class AsignarEmpresaForm(ModelForm):
	class Meta:
		model = Perfil
		fields = ['empresa',]

		widgets = {
			'empresa': forms.TextInput(attrs={'class':'form-title'}),
		}

		
#Formulario para subir archivo

class SubirArchivo(forms.Form):
	file = forms.FileField()

