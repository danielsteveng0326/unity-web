from . import views
from django.urls import path

urlpatterns = [
    path('dash/', views.dash, name="dash"),
    path('cargar/', views.cargar, name="cargar"),
    path('ok/', views.vista_ok, name="ok"),
    
    ]