from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.proveedor_formulario, name='proveedor_formulario'),
    path('consulta/', views.proveedor_consulta, name='proveedor_consulta')
]
