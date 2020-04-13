from django.shortcuts import render
from django.http import HttpResponse
from .models import Equipo, Proceso, Pedido, Proceso, Tarea
from django.views.generic import ListView, DetailView
# Create your views here.


def index(req):
    return HttpResponse("funciono de forma moito gostosa!")


class EquipoListView(ListView):
    model = Equipo
    template_name = 'equipo_lista.html'
    queryset = Equipo.objects.all()
    context_object_name = 'equipos'

    def get_context_data(self, **kwargs):
        context = super(EquipoListView, self).get_context_data(**kwargs)
        # context['titulo_pagina'] = 'Productos'
        return context


class EquipoDetailView(DetailView):
    model = Equipo
    template_name = 'equipo_detalle.html'

    def get_context_data(self, **kwargs):
        context = super(EquipoDetailView, self).get_context_data(**kwargs)
        #context['titulo_pagina'] = 'Detalles del Producto'
        return context


class PedidoListView(ListView):
    model = Pedido
    template_name = 'pedido_lista.html'
    queryset = Pedido.objects.all()
    context_object_name = 'pedidos'

    def get_context_data(self, **kwargs):
        context = super(PedidoListView, self).get_context_data(**kwargs)
        # context['titulo_pagina'] = 'Productos'
        return context


class PedidoDetailView(DetailView):
    model = Pedido
    template_name = 'pedido_detalle.html'

    def get_context_data(self, **kwargs):
        context = super(PedidoDetailView, self).get_context_data(**kwargs)
        #context['titulo_pagina'] = 'Detalles del Producto'
        return context

class ProcesoListView(ListView):
    model = Proceso
    template_name = 'proceso_lista.html'
    queryset = Proceso.objects.all()
    context_object_name = 'procesos'

    def get_context_data(self, **kwargs):
        context = super(ProcesoListView, self).get_context_data(**kwargs)
        # context['titulo_pagina'] = 'Productos'
        return context
    
class ProcesoDetailView(DetailView):
    model = Proceso
    template_name = 'proceso_detalle.html'

    def get_context_data(self, **kwargs):
        context = super(ProcesoDetailView, self).get_context_data(**kwargs)
        #context['titulo_pagina'] = 'Detalles del Producto'
        return context

class TareaListView(ListView):
    model = Tarea
    template_name = 'tarea_lista.html'
    queryset = Tarea.objects.all()
    context_object_name = 'tareas'

    def get_context_data(self, **kwargs):
        context = super(TareaListView, self).get_context_data(**kwargs)
        # context['titulo_pagina'] = 'Productos'
        return context

class TareaDetailView(DetailView):
    model = Tarea
    template_name = 'tarea_detalle.html'

    def get_context_data(self, **kwargs):
        context = super(TareaDetailView, self).get_context_data(**kwargs)
        #context['titulo_pagina'] = 'Detalles del Producto'
        return context
