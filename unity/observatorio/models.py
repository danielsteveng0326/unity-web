from django.db import models

class Observatorio(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='#', null=True)
    enlace = models.URLField()

    def __str__(self):
        return self.titulo
