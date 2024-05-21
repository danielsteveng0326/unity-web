from . import views
from django.urls import path

urlpatterns = [
    path('ver/', views.ver, name="ver"),
    path('obs/', views.crear_obs, name="crear" ),
]
