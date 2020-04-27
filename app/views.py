from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Catalogo, Empleado, Equipo, Proceso, Pedido, Proceso, Tarea,Cliente
from django.views.generic import ListView, DetailView,View
from django.urls import reverse
from app.forms import EmpleadoForm, EquipoForm, TareaForm, RegisterForm, LoginForm    #Tendra que haber al menos uno por cada elemento a crear
from django.contrib.auth import authenticate,login,logout
from .consts import OPERARIO,RESPONABLE,CLIENTE,SUPERUSER
from .sessionHandler import getLoggedCliente,getLoggedEmpleado

# Pagina principal
def index(req):    
    return render(req,"index.html")

# Sesiones
# -Pagina de login
def get_login(req):   
    context={'form':RegisterForm, 'login':LoginForm}
    return render(req,"login.html", context)
    
# -Funcion para hacer el login
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

# -Funcion para hacer el logout
def do_logout(req):
    logout(req)
    return redirect('get_login')

# -Funcion para hacer el registro
def register(req):
    form=RegisterForm(req.POST)
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
   
# Empleados
# -Lista
class EmpleadoListView(View):    
    def get(self, request, *args, **kwargs):
        context = {
            'empleados': Empleado.objects.all(),
            'urlBotonFlotante':reverse('empleado_create')
        }
        return render(request, "empleado_lista.html", context)

# -Detalle
class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'empleado_detalle.html'

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        #context['titulo_pagina'] = 'Detalles del Empleado'
        return context

# -Crear
class EmpleadoCreateView(View):
    def get(self, request, *args, **kwargs):
        form = EmpleadoForm() #Probablemente no importado
        context = {
            'form': form
        }
        return render(request, 'empleado_create.html', context)

    def post(self, req):
        form =EmpleadoForm(req.POST)
        if(form.is_valid()):
            form.save()        
            return redirect('empleado_lista')
        else:
            data=Empleado.objects.all()
            context={'form':form,'Empleados':data}
            return render(req, 'empleado_lista.html', context)



# Equipos
# -Lista
class EquipoListView(View):
    def get(self, request, *args, **kwargs):   
        context = {
            'equipos': Equipo.objects.all(),
            'form': EquipoForm()
        }
        return render(request, "equipo_lista.html", context)

    # El método post deberá ir en el detalle (?)
    def post(self, request, *args, **kwargs): 
        form=EquipoForm(request.POST)
        if form.is_valid():
           form.save()
        return redirect('equipo_lista')
        
# -Detalle       
class EquipoDetailView(DetailView):
    model = Equipo
    template_name = 'equipo_detalle.html'

    def get_context_data(self, **kwargs):
        context = super(EquipoDetailView, self).get_context_data(**kwargs)
        #context['titulo_pagina'] = 'Detalles del Equipo'
        return context

# -Crear
class EquipoCreateView(View):
    def get(self, request, *args, **kwargs):
        form = EquipoForm()
        context = {
            'form': form
        }
        return render(request, 'equipo_create.html', context)


# Pedidos
# -Lista
class PedidoListView(ListView):
    model = Pedido
    template_name = 'pedido_lista.html'
    queryset = Pedido.objects.all()
    context_object_name = 'pedidos'

    def get_context_data(self, **kwargs):
        context = super(PedidoListView, self).get_context_data(**kwargs)
        # context['titulo_pagina'] = 'Pedidos'
        return context

# -Detalle
class PedidoDetailView(DetailView):
    model = Pedido
    template_name = 'pedido_detalle.html'

    def get_context_data(self, **kwargs):
        context = super(PedidoDetailView, self).get_context_data(**kwargs)
        #context['titulo_pagina'] = 'Detalles del Pedido'
        return context

# -Crear: Es diferente porque pedido se crea desde catálogo, por tanto es una función y no una nueva view.
def crear_pedido(req):
    pedido=Pedido()
    pedido.planificado=False
    pedido.producido=False
    pedido.catalogo= Catalogo.objects.get(pk=req.POST['producto'])
    print(pedido.catalogo.precio)
    pedido.cliente=getLoggedCliente(req)
    pedido.importe=pedido.catalogo.precio * int(req.POST["cantidad"])
    pedido.cantidad=int(req.POST['cantidad'])
    pedido.save() 
    return redirect('catalogo_lista')
    #obj = Class.objects.get(pk=this_object_id)

# -Muestra pedidos filtrando para el cliente logueado
def mis_pedidos(req):
    pedidos=Pedido.objects.filter(cliente=getLoggedCliente(req).id)
    context={'pedidos':pedidos}
    return render(req,'pedido_lista.html',context)

# Procesos
# -Lista    
class ProcesoListView(ListView):
    model = Proceso
    template_name = 'proceso_lista.html'
    queryset = Proceso.objects.all()
    context_object_name = 'procesos'

    def get_context_data(self, **kwargs):
        context = super(ProcesoListView, self).get_context_data(**kwargs)
        # context['titulo_pagina'] = 'Procesos'
        return context

# -Detalle
class ProcesoDetailView(DetailView):
    model = Proceso
    template_name = 'proceso_detalle.html'

    def get_context_data(self, **kwargs):
        context = super(ProcesoDetailView, self).get_context_data(**kwargs)
        #context['titulo_pagina'] = 'Detalles del Proceso'
        return context
# -Crear
# [Crear]

# Tareas
# -Lista
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

# -Detalle
class TareaDetailView(DetailView):
    model = Tarea
    template_name = 'tarea_detalle.html'

    def get_context_data(self, **kwargs):
        context = super(TareaDetailView, self).get_context_data(**kwargs)
        #context['titulo_pagina'] = 'Detalles de la Tarea'
        return context
# -Crear
class TareaCreateView(View):
    def get(self, request, *args, **kwargs):
        form = TareaForm() #Probablemente no importado
        context = {
            'form': form
        }
        return render(request, 'tarea_create.html', context)


# Catalogos
# -Lista
class CatalogoListView(ListView):
    model = Catalogo
    template_name = 'catalogo_lista.html'
    queryset = Catalogo.objects.all()
    context_object_name = 'catalogos'

    def get_context_data(self, **kwargs):
        context = super(CatalogoListView, self).get_context_data(**kwargs)
        # context['titulo_pagina'] = 'Catalogos'
        return context

# -Detalle
class CatalogoDetailView(DetailView):
    model = Catalogo
    template_name = 'catalogo_detalle.html'

    def get_context_data(self, **kwargs):
        context = super(CatalogoDetailView, self).get_context_data(**kwargs)
        #context['titulo_pagina'] = 'Detalles del catalogo'
        return context
# -Crear
# [Crear]



