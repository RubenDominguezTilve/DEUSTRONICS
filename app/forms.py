from django import forms
from .models import Equipo, TipoEquipo,Tarea

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