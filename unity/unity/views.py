from django.shortcuts import render

def home_view(request):
  return render(request, "pages/home.html", {})

def proveedores (request):
    return render (request, 'pages/proveedores.html', {})

def calidad (request):
    return render (request, 'pages/gc_mapa.html', {})

def contratacion_dashboard (request):
    return render (request, 'pages/contratacion_dashboard.html', {})