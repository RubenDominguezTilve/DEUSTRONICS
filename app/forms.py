from django import forms
from .models import Equipo

class EquipoForm(forms.Form):
    class Meta:
        model = Equipo
        fields = '__all__'