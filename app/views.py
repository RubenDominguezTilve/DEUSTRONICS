from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Catalogo, Empleado, Equipo, Proceso, Pedido, Proceso, Tarea, Cliente
from django.views.generic import ListView, DetailView,View
from django.urls import reverse
from app.forms import EmpleadoForm, EquipoForm, CatalogoForm, ProcesoForm, PedidoForm, TareaForm, RegisterForm, LoginForm    #Tendra que haber al menos uno por cada elemento a crear
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
    # --La funcion get crea la vista    
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

    # --Funcion para actualizar un elemento en la BBDD
    def post(self, req, *args, **kwargs):
        empeladoUpdate = Empleado()
        empleadoUpdate.dni = str(req.POST['dni'])
        empleadoUpdate.nombre = str(req.POST['nombre'])
        empleadoUpdate.apellido1 = str(req.POST['apellido1'])
        empleadoUpdate.apellido2 = str(req.POST['apellido2'])
        empleadoUpdate.telefono = str(req.POST['telefono'])
        empleadoUpdate.usuario = str(req.POST['usuario'])
       # procesoUpdate.nombre = str(req.POST.get('NombreProceso', 'DEFAULT'))
        empleadoUpdate.save()
        return redirect('empleado_lista')

# -Crear
class EmpleadoCreateView(View):
    # --La funcion get crea la vista
    def get(self, request, *args, **kwargs):
        form = EmpleadoForm()
        context = {
            'form': form
        }
        return render(request, 'empleado_create.html', context)
        
    # --La funcion post permite que el formulario envie los datos y redirija despues
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
    # --La funcion get crea la vista
    def get(self, request, *args, **kwargs):   
        context = {
            'equipos': Equipo.objects.all(),

            'form': EquipoForm(),  #Borrar
            
            'urlBotonFlotante':reverse('equipo_create')
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

    # --Funcion para actualizar un elemento en la BBDD
    def post(self, req, *args, **kwargs):
        equipoUpdate = Equipo()
        equipoUpdate.marca = str(req.POST['equipoMarca'])
        equipoUpdate.modelo = str(req.POST['equipoModelo'])
        equipoUpdate.tipo = TipoEquipo.objects.get(pk=req.POST['equipoTipo'])
        equipoUpdate.fecha_adquisicion = req.POST['equipoAdquisicion']
        equipoUpdate.fecha_instalacion = req.POST['equipoInstalacion']
        equipoUpdate.fecha_ultimo_mantenimiento = req.POST['equipoMantenimiento']
       # procesoUpdate.nombre = str(req.POST.get('NombreProceso', 'DEFAULT'))
        equipoUpdate.save()
        return redirect('equipo_lista')

# -Crear
class EquipoCreateView(View):
    # --La funcion get crea la vista
    def get(self, request, *args, **kwargs):
        form = EquipoForm()
        context = {
            'form': form
        }
        return render(request, 'equipo_create.html', context)
        
    # --La funcion post permite que el formulario envie los datos y redirija despues
    def post(self, req):
        form = EquipoForm(req.POST)
        if(form.is_valid()):
            form.save()        
            return redirect('equipo_lista')
        else:
            data = Equipo.objects.all()
            context = {'form':form,'Equipos':data}
            return render(req, 'equipo_lista.html', context)


# Pedidos
# -Lista
class PedidoListView(View):
    # --La funcion get crea la vista    
    def get(self, request, *args, **kwargs):
        context = {
            'pedidos': Pedido.objects.all(),
            'urlBotonFlotante':reverse('pedido_create_manual')
        }
        return render(request, "pedido_lista.html", context)

# -Detalle
class PedidoDetailView(DetailView):
    model = Pedido
    template_name = 'pedido_detalle.html'

    def get_context_data(self, **kwargs):
        context = super(PedidoDetailView, self).get_context_data(**kwargs)
        #context['titulo_pagina'] = 'Detalles del Pedido'
        return context

    # --Funcion para actualizar un elemento en la BBDD
    def post(self, req, *args, **kwargs):
        pedidoUpdate = Pedido()
        pedidoUpdate.planificado = bool(req.POST['pedidoPlanificado'])
        pedidoUpdate.producido = bool(req.POST['pedidoProducido'])
        pedidoUpdate.cantidad = int(req.POST['pedidoCantidad'])
        pedidoUpdate.catalogo = Catalogo.objects.get(pk=int(req.POST['pedidoReferencia']))
        pedidoUpdate.cliente = Cliente.objects.get(pk=int(req.POST['pedidoCliente']))
        pedidoUpdate.importe = pedidoUpdate.cantidad * pedidoUpdate.catalogo.precio
       # procesoUpdate.nombre = str(req.POST.get('NombreProceso', 'DEFAULT'))
        pedidoUpdate.save()
        return redirect('pedido_lista')

# -Crear: Es diferente porque pedido se crea desde catálogo, por tanto es una función y no una nueva view.
def crear_pedido(req):
    pedido=Pedido()
    pedido.planificado=False
    pedido.producido=False
    pedido.catalogo= Catalogo.objects.get(pk=req.POST['producto'])      #Equivale a pedido.catalogo = catalogo where id == producto(value)
    pedido.cliente=getLoggedCliente(req)
    pedido.importe=pedido.catalogo.precio * int(req.POST["cantidad"])
    pedido.cantidad=int(req.POST['cantidad'])
    pedido.save() 
    return redirect('catalogo_lista')
    #obj = Class.objects.get(pk=this_object_id)

class PedidoCreateView(View):
    # --La funcion get crea la vista
    def get(self, request, *args, **kwargs):
        form = PedidoForm()
        context = {
            'form': form
        }
        return render(request, 'pedido_create.html', context)
        
    # --La funcion post permite que el formulario envie los datos y redirija despues
    def post(self, req):
        form = PedidoForm(req.POST)
        if(form.is_valid()):
            form.save()        
            return redirect('pedido_lista')
        else:
            data = Pedido.objects.all()
            context = {'form':form,'Pedidos':data}
            return render(req, 'pedido_lista.html', context)

# -Muestra pedidos filtrando para el cliente logueado
def mis_pedidos(req):
    pedidos=Pedido.objects.filter(cliente=getLoggedCliente(req).id)
    context={'pedidos':pedidos}
    return render(req,'pedido_lista.html',context)

# Procesos
# -Lista    
class ProcesoListView(View):
    # --La funcion get crea la vista    
    def get(self, request, *args, **kwargs):
        context = {
            'procesos': Proceso.objects.all(),
            'urlBotonFlotante':reverse('proceso_create')
        }
        return render(request, "proceso_lista.html", context)        

# -Detalle
class ProcesoDetailView(DetailView):
    model = Proceso
    template_name = 'proceso_detalle.html'
    # --Funcion para generar la vista con contenido 
    def get_context_data(self, **kwargs):
        context = super(ProcesoDetailView, self).get_context_data(**kwargs)
        #context['titulo_pagina'] = 'Detalles del Proceso'
        return context

    # --Funcion para actualizar un elemento en la BBDD
    def post(self, req, *args, **kwargs):
        procesoUpdate = Proceso()
        procesoUpdate.id = int(req.POST['idProceso'])
        procesoUpdate.nombre = str(req.POST['NombreProceso'])
       # procesoUpdate.nombre = str(req.POST.get('NombreProceso', 'DEFAULT'))
        procesoUpdate.save()
        return redirect('proceso_lista')

# -Crear
class ProcesoCreateView(View):
    # --La funcion get crea la vista
    def get(self, request, *args, **kwargs):
        form = ProcesoForm()
        context = {
            'form': form
        }
        return render(request, 'proceso_create.html', context)
        
    # --La funcion post permite que el formulario envie los datos y redirija despues
    def post(self, req):
        form = ProcesoForm(req.POST)
        if(form.is_valid()):
            form.save()        
            return redirect('proceso_lista')
        else:
            data = Proceso.objects.all()
            context = {'form':form,'Procesos':data}
            return render(req, 'proceso_lista.html', context)

# Tareas
# -Lista
class TareaListView(View):
    # --La funcion get crea la vista
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
    def get_context_data(self, **kwargs):                                   #Prescindible
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

    # --Funcion para actualizar un elemento en la BBDD
    def post(self, req, *args, **kwargs):
        tareaUpdate = Tarea()
        tareaUpdate.id = int(req.POST['tareaID'])
        tareaUpdate.hora_inicio = req.POST['HoraInicioTarea']
        tareaUpdate.hora_fin = req.POST['HoraFinTarea']
        tareaUpdate.equipo = str(req.POST['tareaIDEquipo'])
        tareaUpdate.proceso = str(req.POST['tareaIDProceso'])
        tareaUpdate.pedido = str(req.POST['tareaIDPedido'])
    # tareaUpdate.empleados_asignados = req.POST['empleados_asignados']
       # procesoUpdate.nombre = str(req.POST.get('NombreProceso', 'DEFAULT'))
        tareaUpdate.save()
        return redirect('tarea_lista')

# -Crear
class TareaCreateView(View):
    # --La funcion get crea la vista
    def get(self, request, *args, **kwargs):
        form = TareaForm()
        context = {
            'form': form
        }
        return render(request, 'tarea_create.html', context)
        
    # --La funcion post permite que el formulario envie los datos y redirija despues
    def post(self, req):
        form = TareaForm(req.POST)
        if(form.is_valid()):
            form.save()        
            return redirect('tarea_lista')
        else:
            data = Tarea.objects.all()
            context = {'form':form,'Tareas':data}
            return render(req, 'tarea_lista.html', context)

# Catalogos
# -Lista
class CatalogoListView(View):
    # --La funcion get crea la vista    
    def get(self, request, *args, **kwargs):
        context = {
            'catalogos': Catalogo.objects.all(),
            'urlBotonFlotante':reverse('catalogo_create')
        }
        return render(request, "catalogo_lista.html", context) 

# -Detalle
class CatalogoDetailView(DetailView):
    model = Catalogo
    template_name = 'catalogo_detalle.html'

    def get_context_data(self, **kwargs):
        context = super(CatalogoDetailView, self).get_context_data(**kwargs)
        #context['titulo_pagina'] = 'Detalles del catalogo'
        return context

    # --Funcion para actualizar un elemento en la BBDD
    def post(self, req, *args, **kwargs):
        catalogoUpdate = Catalogo()
        catalogoUpdate.id = int(req.POST['catalogoID'])
        catalogoUpdate.descripcion = str(req.POST['catalogoDescripcion'])
        catalogoUpdate.nombre = str(req.POST['catalogoNombre'])
        catalogoUpdate.precio = float(req.POST['catalogoPrecio'])
       # procesoUpdate.nombre = str(req.POST.get('NombreProceso', 'DEFAULT'))
        catalogoUpdate.save()
        return redirect('catalogo_lista')

# -Crear
class CatalogoCreateView(View):
    # --La funcion get crea la vista
    def get(self, request, *args, **kwargs):
        form = CatalogoForm()
        context = {
            'form': form
        }
        return render(request, 'catalogo_create.html', context)
        
    # --La funcion post permite que el formulario envie los datos y redirija despues
    def post(self, req):
        form = CatalogoForm(req.POST)
        if(form.is_valid()):
            form.save()        
            return redirect('catalogo_lista')
        else:
            data = Catalogo.objects.all()
            context = {'form':form,'Catalogos':data}
            return render(req, 'catalogo_lista.html', context)



