from . import views
from django.urls import path

## acá tengo mis endpoints, el cuál me permite moverme dentro de la app
### dash me muestra la pagina principal
#### cargar me carga el archivo .csv que está en la carpeta static

urlpatterns = [
    path('dash/', views.dash, name="dash"),
    path('cargar/', views.cargar, name="cargar"),
    path('ok/', views.vista_ok, name="ok"),
    
    ]