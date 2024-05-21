from django.shortcuts import render
from . models import Observatorio
from django.utils import timezone
from django.http import HttpResponse



def ver(request):

    observatorios = Observatorio.objects.all()

    return render(request, 'pages/observatorio.html', {'observatorios': observatorios})

def crear_obs(request):

    observatorio_1 = Observatorio(
        titulo = "Observatorio Secretaría de Salud",
        subtitulo = "Mapa de Cobertura en Salud",
        descripcion = "La Secretaría de salud.",
        fecha = timezone.now(),
        imagen= "/static/img/obs_1.jpeg" ,
        enlace= "#"
    )
    observatorio_1.save()

    observatorio_2 = Observatorio(
        titulo = "Observatorio Secretaría de Planeación",
        subtitulo = "Control de Licencias",
        descripcion = " la oficina de planeación ",
        fecha = timezone.now(),
        imagen= "/static/img/obs_2.jpeg" ,
        enlace= "#"
    )
    observatorio_2.save()

    observatorio_3 = Observatorio(
        titulo = "Observatorio Secretaría de Talento Humano",
        subtitulo = "Listado de Nuestros Servidores",
        descripcion = "La Secretaría de talento humano con el fin de garantizar el buen servicio.",
        fecha = timezone.now(),
        imagen= "/static/img/obs_3.jpeg" ,
        enlace= "#"
    )
    observatorio_3.save()

    return HttpResponse("Listo!")