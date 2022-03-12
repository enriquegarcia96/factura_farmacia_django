import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views import View
from .models import Persona, Categoria, Producto

# Create your views here.


class RegistroCliente(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # Guarda un nuevo cliente
    def post(self, request):
        jd = json.loads(request.body)
        Persona.objects.create(nombre=jd['nombre'], apellido=jd['apellido'], direccion=jd['direccion'], telefono=jd[
                               'telefono'], genero=jd['genero'], numero_identidad=jd['numero_identidad'])
        resp = {'mensaje': 'Acompletado'}
        return JsonResponse(resp)

    # encuentra un usuario
    def get(self, request, id):
        buscarUsuario = list(Persona.objects.filter(
            numero_identidad=id).values())
        usuario = buscarUsuario[0]
        datos = {'mensaje': 'Usuario encontrado', 'Usuario': usuario}
        return JsonResponse(datos)


class FacturaView(View):

    def get(self, request):
        companies = list(Persona.objects.values())
        if len(companies) > 0:
            datos = {'mensaje': 'completado', 'compañias': companies}
        else:
            datos = {'mensaje': 'error'}
        return JsonResponse(datos)


class Factura_de_compra(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        print(request.body)

        datos = {'Mensaje': 'SSIIIIIUUU'}

        return JsonResponse(datos)


# Categoria
class Registro_categoria(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        dato = json.loads(request.body)
        Categoria.objects.create(
            nombre=dato['nombre'], descripcion=dato['descripcion'])
        datos = {'mensaje': 'Completado'}

        return JsonResponse(datos)

    def get(self, request, id=0):

        if(id > 0):
            categorias = list(Categoria.objects.filter(id=id).values())
            if len(categorias) > 0:
                categoria = categorias[0]
                datos = {'Mensaje': 'Completado', 'Categoria': categoria}
            else:
                datos = {'Mensaje': 'Categoria no encontrada'}
            return JsonResponse(datos)
        else:
            categorias = list(Categoria.objects.values())
            if len(categorias) > 0:
                datos = {'Mensaje': 'Completado', 'Categoria': categorias}
            else:
                datos = {'mensaje': 'Categorias no encontrada'}
            return JsonResponse(datos)


# arreglar el problema de categoria id
class Registro_Producto(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        producto = json.loads(request.body)
        print("aquiiii", producto)
        Producto.objects.create(Categoria.objects.get(id=producto['categoria_categoria_id']), precio_venta=producto['precio_venta'], precio_costo=producto['precio_costo'],
                                nombre_producto=producto['nombre_producto'], descripcion=producto['descripcion'], fecha_elaboracion=producto['fecha_elaboracion'], fecha_vencimiento=producto['fecha_vencimiento'])
        resp = {'Mensaje': 'Completado', "Producto": producto}
        return JsonResponse(resp)


class Factura_detalle(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        # relacion con factura y producto

        pass
