from django.contrib import admin
from django.urls import path
from django.conf import settings
from . import views
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('proveedores/', views.proveedores, name = 'proveedores'),
    path('gestion_calidad/', views.calidad, name = 'calidad'),
    path('proveedor/', include ('proveedores.urls')),
    path('observatorio/', include ('observatorio.urls')),
    path('contratacion/', include ('contratacion_dashboard.urls')),
    path('contratacion/', views.contratacion_dashboard, name = 'dashboard'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)