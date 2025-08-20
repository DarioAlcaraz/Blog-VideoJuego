from django import forms
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'nombre',
            'apellido',
            'fecha_nacimiento',
            'imagen',
            'genero',
        ]
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_superuser = False
        user.is_staff = False
        if commit:
            user.save()
        return user
    
class ActualizarUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'nombre',
            'apellido',
            'email',
            'fecha_nacimiento',
            'imagen',
            'genero',
        ]
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }


   