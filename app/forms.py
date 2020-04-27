from django import forms
from .models import Equipo, TipoEquipo,Tarea
from django.contrib.auth.models import User
class EquipoForm(forms.ModelForm):
    # marca=forms.CharField(max_length=100)
    # modelo=forms.CharField(max_length=100)
    # tipo= forms.ModelChoiceField(queryset=TipoEquipo.objects.all())
    # fecha_adquisicion=forms.DateField()
    # fecha_instalacion=forms.DateField()
    # fecha_ultimo_mantenimiento=forms.DateField()
    class Meta:
        model=Equipo
        fields = '__all__'


class TareaForm(forms.ModelForm):
    class Meta:
        model=Tarea
        fields = '__all__'

class RegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields = ('username','password','email')

class LoginForm(forms.Form):
    username=forms.CharField(max_length=100)
    
    attrs = {
        "type": "password"
    }
    password = forms.CharField(widget=forms.TextInput(attrs=attrs))