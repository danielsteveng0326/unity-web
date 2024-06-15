from django.urls import path
from . import views

### en mi plantilla mas adelante veremos que los dos endpoints que tengo, están renderizados en 2 botones
## que nos lleva  a la opción seleccionada

urlpatterns = [
    path('crear/', views.proveedor_formulario, name='proveedor_formulario'),
    path('consulta/', views.proveedor_consulta, name='proveedor_consulta')
]
