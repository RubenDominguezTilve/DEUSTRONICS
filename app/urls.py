from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    #Pagina Principal
    path('', login_required(views.index), name='index'),

    #Empleados
    path('empleados/', login_required(views.EmpleadoListView.as_view()), name='empleado_lista'),
    path('empleado/<int:pk>/', login_required(views.EmpleadoDetailView.as_view()), name='empleado_detalle'),
    path('empleado/create/', login_required(views.EmpleadoCreateView.as_view()), name='empleado_create'),

    #Equipos 
    path('equipos/', login_required(views.EquipoListView.as_view()), name='equipo_lista'),
    path('equipo/<int:pk>/', login_required(views.EquipoDetailView.as_view()), name='equipo_detalle'),
    path('equipo/create/', login_required(views.EquipoCreateView.as_view()), name='equipo_create'),

    #Pedidos
    path('pedidos/', login_required(views.PedidoListView.as_view()), name='pedido_lista'),
    path('pedido/<int:pk>/', login_required(views.PedidoDetailView.as_view()), name='pedido_detalle'),
    path('pedido/create/', login_required(views.crear_pedido), name='pedido_create'),
    path('misPedidos/', login_required(views.mis_pedidos), name='mis_pedidos'),

    #Procesos
    path('procesos/', login_required(views.ProcesoListView.as_view()), name='proceso_lista'),
    path('proceso/<int:pk>/', login_required(views.ProcesoDetailView.as_view()),name='proceso_detalle'),
    path('proceso/create/', login_required(views.ProcesoCreateView.as_view()), name='proceso_create'),

    #Tareas
    path('tareas/', login_required(views.TareaListView.as_view()), name='tarea_lista'),
    path('tarea/<int:pk>/', login_required(views.TareaDetailView.as_view()), name='tarea_detalle'),
    path('tarea/create/', login_required(views.TareaCreateView.as_view()), name='tarea_create'),

    #Catalogos
    path('catalogo/', login_required(views.CatalogoListView.as_view()), name='catalogo_lista'),
    path('catalogo/<int:pk>/', login_required(views.CatalogoDetailView.as_view()), name='catalogo_detalle'),
    path('catalogo/create/', login_required(views.CatalogoCreateView.as_view()), name='catalogo_create'),
  

    #Login
    path('login/', views.get_login, name='get_login'),
    path('register/', views.register, name='do_register'),
    path('logout/', views.do_logout, name='logout'),
    path('dologin/', views.do_login, name='do_login'),


]
