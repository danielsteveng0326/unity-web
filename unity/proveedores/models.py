from django.db import models

## éste modulo o servicio de mi aplicación lo que hace es tratat el registro a mi base de datos
## cada uno de los proveedores ingresados por el usuario
## es importante resaltar que el usuario NO tiene la opción de modificar, ni alterar, ni cambiar
## la información luego de ser suministrada
class Proveedor(models.Model):
    PERSONA_NATURAL = '1'
    PERSONA_JURIDICA = '2'
    OPCIONES_PERSONA = [
        (PERSONA_NATURAL, 'Persona Natural'),
        (PERSONA_JURIDICA, 'Persona Jurídica'),
    ]

    nombre_razon_social = models.CharField(max_length=100)
    nit = models.CharField(max_length=20, primary_key=True)
    nombre_rep_legal = models.CharField(max_length=100)
    identificacion = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100)
    correo = models.EmailField()
    opcion_persona = models.CharField(max_length=1, choices=OPCIONES_PERSONA)
    

    def save(self, *args, **kwargs):
        if self.opcion_persona == self.PERSONA_NATURAL:
            self.nombre_razon_social = self.nombre_rep_legal
            self.nit = self.identificacion
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre_razon_social