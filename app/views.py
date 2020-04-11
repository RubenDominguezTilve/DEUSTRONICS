from django.shortcuts import render
from django.http import HttpResponse
from .models import Equipo
from django.views.generic import ListView, DetailView
# Create your views here.


def index(req):
    return HttpResponse("funciono de forma moito gostosa!")


class EquiposListView(ListView):
    model = Equipo
    template_name = 'equipo_lista.html'
    queryset = Equipo.objects.all()
    context_object_name = 'equipos'

    def get_context_data(self, **kwargs):
        context = super(EquiposListView, self).get_context_data(**kwargs)
        # context['titulo_pagina'] = 'Productos'
        return context


class EquipoDetailView(DetailView):
    model = Equipo
    template_name = 'equipo_detalle.html'

    def get_context_data(self, **kwargs):
        context = super(EquipoDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles del Producto'
        return context
