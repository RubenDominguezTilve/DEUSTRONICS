from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('empleados/', views.EmpleadoListView.as_view(), name='empleado_lista'),
    path('empleado/<int:pk>/', views.EmpleadoDetailView.as_view(), name='empleado_detalle'),
    path('equipos/', views.EquipoListView.as_view(), name='equipo_lista'),
    path('equipo/<int:pk>/', views.EquipoDetailView.as_view(), name='equipo_detalle'),
    path('equipo/create/', views.EquipoCreateView.as_view(), name='equipo_create'),
    path('pedidos/', views.PedidoListView.as_view(), name='pedido_lista'),
    path('pedido/<int:pk>/', views.PedidoDetailView.as_view(), name='pedido_detalle'),
    path('procesos/', views.ProcesoListView.as_view(), name='proceso_lista'),
    path('proceso/<int:pk>/', views.ProcesoDetailView.as_view(),
         name='proceso_detalle'),
    path('tareas/', views.TareaListView.as_view(), name='tarea_lista'),
    path('tarea/<int:pk>/', views.TareaDetailView.as_view(), name='tarea_detalle'),
    path('catalogo/', views.CatalogoListView.as_view(), name='catalogo_lista'),
    path('catalogo/<int:pk>/', views.CatalogoDetailView.as_view(), name='catalogo_detalle'),


]
