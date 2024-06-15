from . import views
from django.urls import path

### el endpoint ver nos lleva como resultado todos los observatorio que hemos creado
#### de manera manual, tengo una función en el archivo views.py que veremos luego para guardar cada
# observatorio

urlpatterns = [
    path('ver/', views.ver, name="ver"),
    path('obs/', views.crear_obs, name="crear" ),
]
