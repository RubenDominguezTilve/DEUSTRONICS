from django.shortcuts import render
from django.http import HttpResponse
from .models import Catalogo, Empleado, Equipo, Proceso, Pedido, Proceso, Tarea
from django.views.generic import ListView, DetailView,View
from app.forms import EquipoForm
# Create your views here.


def index(req):
    return render(req,"index.html")


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


class EquipoListView(ListView):
    model = Equipo
    template_name = 'equipo_lista.html'
    queryset = Equipo.objects.all()
    context_object_name = 'equipos'
    context={}
    context["equipos"]=Equipo.objects.all()
    context['form'] = EquipoForm()

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


class TareaListView(ListView):
    model = Tarea
    template_name = 'tarea_lista.html'
    queryset = Tarea.objects.all()
    context_object_name = 'tareas'

    def post(self, req):
        print(req.POST["text"])
        
        return HttpResponse("todo OK jose luis")
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