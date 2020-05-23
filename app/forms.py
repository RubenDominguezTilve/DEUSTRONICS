from django import forms
from .models import Equipo, TipoEquipo, Tarea, Empleado, Proceso, Catalogo, Cliente, Pedido
from django.contrib.auth.models import User
from app.widgets.formWidgets import DateInput


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
        widgets = { 'fecha_adquisicion' : DateInput(),'fecha_instalacion':DateInput(),'fecha_ultimo_mantenimiento':DateInput()} 

# Formulario crear Tareas
class TareaForm(forms.ModelForm):
    class Meta:
        model=Tarea
        fields = '__all__'
        widgets = {
            'hora_inicio': forms.TextInput(attrs={'pattern': "[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}", "placeholder":"yyyy-mm-dd hh:mm"}),
            'hora_fin': forms.TextInput(attrs={'pattern': "[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}", "placeholder":"yyyy-mm-dd hh:mm"}),
        }

# Formulario crear Catalogos
class CatalogoForm(forms.ModelForm):
    class Meta:
        model=Catalogo
        fields = '__all__'
        
      


# Formulario crear Pedidos
class PedidoForm(forms.ModelForm):
    class Meta:
        model=Pedido
        fields = '__all__'
        widgets = {
            'importe': forms.HiddenInput()
        }

# Formulario crear Procesos
class ProcesoForm(forms.ModelForm):
    class Meta:
        model=Proceso
        fields = '__all__'


# Formulario de Registro
class RegisterForm(forms.Form):
    username=forms.CharField(max_length=100)
    password1 = forms.CharField(widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(widget=forms.PasswordInput, required=True)
    empresa=forms.CharField(max_length=100)
    


# Formulario de Inicio de Sesion
class LoginForm(forms.Form):
    # Usuario
    username=forms.CharField(max_length=100)
    
    # Contraseña
    attrs = {
        "type": "password" # Atributo para mostrarlo como contraseña
    }
    password = forms.CharField(widget=forms.TextInput(attrs=attrs))