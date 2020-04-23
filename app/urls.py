from django.urls import path
from . import views

urlpatterns = [
    #Pagina Principal
    path('', views.index, name='index'),
    #Empleados
    path('empleados/', views.EmpleadoListView.as_view(), name='empleado_lista'),
    path('empleado/<int:pk>/', views.EmpleadoDetailView.as_view(), name='empleado_detalle'),
    #Equipos
    path('equipos/', views.EquipoListView.as_view(), name='equipo_lista'),
    path('equipo/<int:pk>/', views.EquipoDetailView.as_view(), name='equipo_detalle'),
    path('equipo/create/', views.EquipoCreateView.as_view(), name='equipo_create'),
    #Pedidos
    path('pedidos/', views.PedidoListView.as_view(), name='pedido_lista'),
    path('pedido/<int:pk>/', views.PedidoDetailView.as_view(), name='pedido_detalle'),
    #Procesos
    path('procesos/', views.ProcesoListView.as_view(), name='proceso_lista'),
    path('proceso/<int:pk>/', views.ProcesoDetailView.as_view(),name='proceso_detalle'),
    #Tareas
    path('tareas/', views.TareaListView.as_view(), name='tarea_lista'),
    path('tarea/<int:pk>/', views.TareaDetailView.as_view(), name='tarea_detalle'),
    path('tarea/create/', views.TareaListView.as_view(), name='tarea_create'),
    #Catalogos
    path('catalogo/', views.CatalogoListView.as_view(), name='catalogo_lista'),
    path('catalogo/<int:pk>/', views.CatalogoDetailView.as_view(), name='catalogo_detalle'),
    path('catalogo/<int:pk>/', views.CatalogoDetailView.as_view(), name='catalogo_detalle'),

    #Login
    path('login/', views.get_login, name='get_login'),
     path('register/', views.register, name='register'),


]
