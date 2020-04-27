from django import forms
from .models import Equipo, TipoEquipo, Tarea, Empleado, Proceso, Catalogo, Cliente, Pedido
from django.contrib.auth.models import User



# Formulario crear Empleados
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model=Empleado
        fields = '__all__'


# Formulario crear Equipos
class EquipoForm(forms.ModelForm):
    class Meta:
        model=Equipo
        fields = '__all__'


# Formulario crear Tareas
class TareaForm(forms.ModelForm):
    class Meta:
        model=Tarea
        fields = '__all__'


# Formulario de Registro
class RegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields = ('username','password','email')


# Formulario de Inicio de Sesion
class LoginForm(forms.Form):
    # Usuario
    username=forms.CharField(max_length=100)
    
    # Contraseña
    attrs = {
        "type": "password" # Atributo para mostrarlo como contraseña
    }
    password = forms.CharField(widget=forms.TextInput(attrs=attrs))