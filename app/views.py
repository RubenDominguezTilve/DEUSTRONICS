from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Catalogo, Empleado, Equipo, Proceso, Pedido, Proceso, Tarea
from django.views.generic import ListView, DetailView,View
from django.urls import reverse
from app.forms import EquipoForm, TareaForm, UserForm, LoginForm
from django.contrib.auth import authenticate,login,logout
from .consts import OPERARIO,RESPONABLE,CLIENTE,SUPERUSER
# Create your views here.


def index(req):    
    return render(req,"index.html")

def get_login(req):   
    context={'form':UserForm, 'login':LoginForm}
    return render(req,"login.html", context)
    
def do_login(req):
    print('lego aqui')
    username = req.POST['username']
    password = req.POST['password']
    user = authenticate(req, username=username, password=password)
    if user is not None:
        login(req, user)
        print('bien')
        print(req.GET)
        return redirect('index')
    else:
        print('mal')
        return redirect('get_login')
def do_logout(req):
    logout(req)
    return redirect('get_login')

    
def register(req):
    form=UserForm(req.POST)
    if(form.is_valid):
        form.save()
        # user=authenticate(req,username=form.cleaned_data['username'],password=form.cleaned_data['password'])
        # if user is not None:
        #     login(req, user)
        print("valido")
        return redirect('index')
    else:
        print("no valido")
        return redirect('get_login')
   

class EmpleadoListView(ListView):
    model = Empleado
    template_name = 'empleado_lista.html'
    queryset = Empleado.objects.all()
    context_object_name = 'empleados'

    def get_context_data(self, **kwargs):
        context = super(EmpleadoListView, self).get_context_data(**kwargs)
        # context['titulo_pagina'] = 'Empleados'
        return context


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'empleado_detalle.html'

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        #context['titulo_pagina'] = 'Detalles del Empleado'
        return context


class EquipoListView(View):
    # model = Equipo
    # template_name = 'equipo_lista.html'
    # queryset = Equipo.objects.all()
    # context_object_name = 'equipos'
    # context={}
    # context["equipos"]=Equipo.objects.all()
    # context['form'] = EquipoForm()


    def get(self, request, *args, **kwargs):   
        context = {
            'equipos': Equipo.objects.all(),
            'form': EquipoForm()
        }
        return render(request, "equipo_lista.html", context)

    def post(self, request, *args, **kwargs): 
        form=EquipoForm(request.POST)
        if form.is_valid():
           form.save()
        return redirect('equipo_lista')
    
    # def get_context_data(self, **kwargs):
    #     context = super(EquipoListView, self).get_context_data(**kwargs)
    #     context['form'] = EquipoForm()
    #     context['text'] ="buenardo"

    #     return context
class EquipoDetailView(DetailView):
    model = Equipo
    template_name = 'equipo_detalle.html'

    def get_context_data(self, **kwargs):
        context = super(EquipoDetailView, self).get_context_data(**kwargs)
        #context['titulo_pagina'] = 'Detalles del Equipo'
        return context
class EquipoCreateView(View):
    def get(self, request, *args, **kwargs):
        form = EquipoForm()
        context = {
            'form': form,
            'titulo_pagina': 'Crear nuevo producto'
        }
        return render(request, 'equipo_create.html', context)



class PedidoListView(ListView):
    model = Pedido
    template_name = 'pedido_lista.html'
    queryset = Pedido.objects.all()
    context_object_name = 'pedidos'

    def get_context_data(self, **kwargs):
        context = super(PedidoListView, self).get_context_data(**kwargs)
        # context['titulo_pagina'] = 'Pedidos'
        return context


class PedidoDetailView(DetailView):
    model = Pedido
    template_name = 'pedido_detalle.html'

    def get_context_data(self, **kwargs):
        context = super(PedidoDetailView, self).get_context_data(**kwargs)
        #context['titulo_pagina'] = 'Detalles del Pedido'
        return context

def crear_pedido(req):
    
class ProcesoListView(ListView):
    model = Proceso
    template_name = 'proceso_lista.html'
    queryset = Proceso.objects.all()
    context_object_name = 'procesos'

    def get_context_data(self, **kwargs):
        context = super(ProcesoListView, self).get_context_data(**kwargs)
        # context['titulo_pagina'] = 'Procesos'
        return context


class ProcesoDetailView(DetailView):
    model = Proceso
    template_name = 'proceso_detalle.html'

    def get_context_data(self, **kwargs):
        context = super(ProcesoDetailView, self).get_context_data(**kwargs)
        #context['titulo_pagina'] = 'Detalles del Proceso'
        return context


class TareaListView(View):
    model = Tarea
    template_name = 'tarea_lista.html'
    queryset = Tarea.objects.all()
    context_object_name = 'tareas'  

    def get(self, req, *args, **kwargs):
        form =TareaForm()
        data=Tarea.objects.all()
        context={'form':form,'tareas':data, 'urlBotonFlotante':reverse('tarea_create')}
        return render(req, 'tarea_lista.html', context)

    def post(self, req):
        form =TareaForm(req.POST)
        if(form.is_valid()):
            form.save()        
            return redirect('tarea_lista')
        else:
            
            data=Tarea.objects.all()
            context={'form':form,'tareas':data}
            return render(req, 'tarea_lista.html', context)
    def get_context_data(self, **kwargs):
        context = super(TareaListView, self).get_context_data(**kwargs)
        # context['titulo_pagina'] = 'Tareas'
        return context


class TareaDetailView(DetailView):
    model = Tarea
    template_name = 'tarea_detalle.html'

    def get_context_data(self, **kwargs):
        context = super(TareaDetailView, self).get_context_data(**kwargs)
        #context['titulo_pagina'] = 'Detalles de la Tarea'
        return context


class CatalogoListView(ListView):
    model = Catalogo
    template_name = 'catalogo_lista.html'
    queryset = Catalogo.objects.all()
    context_object_name = 'catalogos'

    def get_context_data(self, **kwargs):
        context = super(CatalogoListView, self).get_context_data(**kwargs)
        # context['titulo_pagina'] = 'Catalogos'
        return context


class CatalogoDetailView(DetailView):
    model = Catalogo
    template_name = 'catalogo_detalle.html'

    def get_context_data(self, **kwargs):
        context = super(CatalogoDetailView, self).get_context_data(**kwargs)
        #context['titulo_pagina'] = 'Detalles del catalogo'
        return context


