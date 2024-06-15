from django.shortcuts import render
from .forms import ProveedorForm
from .models import Proveedor

## con ésta primera funcion, vamos a comunicar con el método POST el ingreso de la información
## suministrada por el usuario y luego será ingresada a nuestra base de datos SQL


def proveedor_formulario(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return render (request, 'pages/proveedores.html', {})
            # Aquí podrías redirigir a una página de éxito o hacer cualquier otra acción
    else:
        form = ProveedorForm()

    return render(request, 'pages/crear_proveedor.html', {'form': form})


##en ésta segunda función vamos a traer mas adelante los resultados de las consultas realizadas
## por el usuario

def proveedor_consulta(request):
    proveedors_all = Proveedor.objects.all()
    if request.method == 'POST':
        element_nit = request.POST['nit']
        proveedors = Proveedor.objects.get(nit = element_nit )
        
        return render(request, 'pages/buscar_proveedor.html', {'proveedors': proveedors, 'proveedors_all': proveedors_all})
    else:

        return render(request, 'pages/buscar_proveedor.html', {'proveedors_all': proveedors_all})




#def proveedor_consulta2(request):
#    
#    proveedors = Proveedor.objects.all()
#    proveedors_1 = Proveedor.objects.filter(correo = 'victor@empresa.com')
#    proveedors_2 = Proveedor.objects.get(id = 1)
#    
#    return render(request, 'pages/buscar_proveedor.html', {'proveedors': proveedors, 'proveedors_1':proveedors_1, 
#                                                'proveedors_2': proveedors_2})


