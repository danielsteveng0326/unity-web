from django.shortcuts import render
from .utils import cargar_datos_desde_csv
from django.http import HttpResponse
from .models import Contrato
from django.db.models import Sum, Count

## acá encontramos las vistas que renderizaremos y mostraremos a través de nuestras plantillas de HTML

def cargar(request):
    cargar_datos_desde_csv()
    return render (request, 'pages/ok.html', {})

def dash (request):

    suma_valor_del_contrato = Contrato.objects.aggregate(Sum('valor_del_contrato'))['valor_del_contrato__sum']
    numero_de_registros = Contrato.objects.count()
    
    suma_valor_del_contrato = suma_valor_del_contrato//1000000
    
    context = {
            'suma_valor_del_contrato': suma_valor_del_contrato,
            'numero_de_registros': numero_de_registros,
        }

    

    return render (request, 'pages/contratacion_dashboard.html', context)


def vista_ok (request):
    return render (request, 'pages/ok.html', {})

def vista_f (request):
    return render (request, 'pages/f.html', {})