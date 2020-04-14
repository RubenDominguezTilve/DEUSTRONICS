from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('equipos/', views.EquipoListView.as_view(), name='equipos_lista'),
    path('equipo/<int:pk>/', views.EquipoDetailView.as_view(), name='equipo_detalle'),
    path('pedidos/', views.PedidoListView.as_view(), name='pedidos_lista'),
    path('pedido/<int:pk>/', views.PedidoDetailView.as_view(), name='pedido_detalle'),
    path('procesos/', views.ProcesoListView.as_view(), name='procesos_lista'),
    path('proceso/<int:pk>/', views.ProcesoDetailView.as_view(),
         name='proceso_detalle'),
    path('tareas/', views.TareaListView.as_view(), name='tareas_lista'),
    path('tarea/<int:pk>/', views.TareaDetailView.as_view(), name='tarea_detalle'),


]
