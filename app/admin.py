from django.contrib import admin
from .models import  Empleado, Equipo, Tarea, Proceso, Pedido, Catalogo, Cliente, TipoEquipo
# Register your models here.

admin.site.register(Empleado)

admin.site.register(Equipo)
admin.site.register(Tarea)

admin.site.register(Proceso)
admin.site.register(Pedido)

admin.site.register(Catalogo)
admin.site.register(Cliente)
admin.site.register(TipoEquipo)
