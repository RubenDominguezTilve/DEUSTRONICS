from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('equipos/', views.EquiposListView.as_view(), name='equipos_lista'),
    path('equipo/<int:pk>/', views.EquipoDetailView.as_view(), name='equipo_detalle'),

]
