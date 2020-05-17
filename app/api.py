from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Catalogo, Empleado, Equipo, Proceso, Pedido, Proceso, Tarea, Cliente,TipoEquipo
from django.contrib.auth.models import User,Group
from django.views.generic import ListView, DetailView,View
from django.urls import reverse
from app.forms import EmpleadoForm, EquipoForm, CatalogoForm, ProcesoForm, PedidoForm, TareaForm, RegisterForm, LoginForm    #Tendra que haber al menos uno por cada elemento a crear
from django.contrib.auth import authenticate,login,logout
from .consts import OPERARIO,RESPONABLE,CLIENTE,SUPERUSER
from .sessionHandler import getLoggedCliente, getLoggedEmpleado, getTipoUsuario
from django.forms.models import model_to_dict

#Catalogos
#Generar vista modificable de productos
def catalogo_lista_ajax(req):
    productos=Catalogo.objects.all() 
    contexto = {
        "productos" : list(productos.values()),
        "cliente" : getTipoUsuario(req) == CLIENTE
    }
    return JsonResponse(contexto, safe=False)


#Tareas
#Funcion para marcar tarea como realizada en la BBDD
def marcar_tarea(req):
    tarea=Tarea.objects.get(pk=req.POST["idtarea"])
    tarea.finalizada=True
    tarea.save()    
    #return JsonResponse(list(tarea.values()), safe=False)
    return HttpResponse("ok")