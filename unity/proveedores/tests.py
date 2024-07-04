from django.test import TestCase
from .models import Proveedor
from django.urls import reverse
from .forms import ProveedorForm

class ProveedorModelTest(TestCase):

    ## esta función me creará dos proveedores, uno persona natural y otro persona jurídica
    ## con el fin de usarlos en las pruebas unitarias

    def setUp(self):
        self.proveedor_natural = Proveedor.objects.create(
            nombre_razon_social='Juan Perez',
            nit='123456789',
            nombre_rep_legal='Juan Perez',
            identificacion='123456789',
            telefono='555-5555',
            direccion='Calle Falsa 123',
            ciudad='Ciudad X',
            correo='juan@example.com',
            opcion_persona=Proveedor.PERSONA_NATURAL
        )
        self.proveedor_juridico = Proveedor.objects.create(
            nombre_razon_social='Empresa S.A.',
            nit='987654321',
            nombre_rep_legal='Carlos Lopez',
            identificacion='987654321',
            telefono='555-5556',
            direccion='Avenida Siempre Viva 456',
            ciudad='Ciudad Y',
            correo='empresa@example.com',
            opcion_persona=Proveedor.PERSONA_JURIDICA
        )

    ## luego de la creación de los usuarios anteriores, verifica que los datos estén correctos
    def test_proveedor_creation(self):
        self.assertEqual(self.proveedor_natural.nombre_razon_social, 'Juan Perez')
        self.assertEqual(self.proveedor_juridico.nombre_razon_social, 'Empresa S.A.')

    ## dentro de la definición de los modelos migrados a mi base de datos y en las bases del negocio
    ## está establecido que en caso de que el usuario sea persona natural, el campo razon social
    ## contiene el mismo nombre del campo representante legal
    ## ésto corresponde a la normalización de mi base de datos de proveedores

    def test_persona_natural_save(self):
        proveedor = Proveedor.objects.get(nit='123456789')
        self.assertEqual(proveedor.nombre_razon_social, proveedor.nombre_rep_legal)

    ## verificamos que la razón social corresponda a la registrada anteriormente
    def test_persona_juridica_save(self):
        proveedor = Proveedor.objects.get(nit='987654321')
        self.assertEqual(proveedor.nombre_razon_social, 'Empresa S.A.')

class ProveedorFormTest(TestCase):

    ## aquí haremos una evaluación del formulario para el usuario con el fin 
    ## de testear su función
    ## para éste caso haremos un registro "bueno" o correcto con el fin de evaluar si
    ## realmente el formulario responde de manera válida

    def test_valid_form(self):
        data = {
            'nombre_razon_social': 'Empresa S.A.',
            'nit': '987654321',
            'nombre_rep_legal': 'Carlos Lopez',
            'identificacion': '987654321',
            'telefono': '555-5556',
            'direccion': 'Avenida Siempre Viva 456',
            'ciudad': 'Ciudad Y',
            'correo': 'empresa@example.com',
            'opcion_persona': Proveedor.PERSONA_JURIDICA
        }
        form = ProveedorForm(data=data)
        self.assertTrue(form.is_valid())


    ## aquí vamos a intentat testear nuestro formulario vacío
    ## aquí verificamos que nuestro formulario es inválido con datos que no correspondan

    def test_invalid_form(self):
        data = {
            'nombre_razon_social': '',
            'nit': '',
            'nombre_rep_legal': '',
            'identificacion': '',
            'telefono': '',
            'direccion': '',
            'ciudad': '',
            'correo': '',
            'opcion_persona': ''
        }
        form = ProveedorForm(data=data)
        self.assertFalse(form.is_valid())

class ProveedorViewsTest(TestCase):

    def setUp(self):
        self.proveedor = Proveedor.objects.create(
            nombre_razon_social='Empresa S.A.',
            nit='987654321',
            nombre_rep_legal='Carlos Lopez',
            identificacion='987654321',
            telefono='555-5556',
            direccion='Avenida Siempre Viva 456',
            ciudad='Ciudad Y',
            correo='empresa@example.com',
            opcion_persona=Proveedor.PERSONA_JURIDICA
        )

    ## testeamos la función del método GET de mi formulario
    def test_proveedor_formulario_get(self):
        response = self.client.get(reverse('proveedor_formulario'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/crear_proveedor.html')

    ## testeamos la función del método POST de mi formulario
    def test_proveedor_formulario_post(self):
        data = {
            'nombre_razon_social': 'Nueva Empresa',
            'nit': '111222333',
            'nombre_rep_legal': 'Nuevo Representante',
            'identificacion': '111222333',
            'telefono': '555-5557',
            'direccion': 'Nueva Dirección 789',
            'ciudad': 'Ciudad Z',
            'correo': 'nueva@example.com',
            'opcion_persona': Proveedor.PERSONA_JURIDICA
        }
        response = self.client.post(reverse('proveedor_formulario'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/proveedores.html')
        self.assertTrue(Proveedor.objects.filter(nit='111222333').exists())

    ##test del get con el fin de evaluar si mi proveedor se carga correctamente
    def test_proveedor_consulta_get(self):
        response = self.client.get(reverse('proveedor_consulta'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/buscar_proveedor.html')

    ## comprobamos acá que la vista de la consulta devuelve el proveedor que correspondo al nit ingresado
    def test_proveedor_consulta_post(self):
        response = self.client.post(reverse('proveedor_consulta'), {'nit': '987654321'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/buscar_proveedor.html')
        self.assertContains(response, 'Empresa S.A.')

