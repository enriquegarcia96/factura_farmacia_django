import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views import View
from .models import Persona, Categoria

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


class FacturaNueva(View):

    # todo: hacer la relacion con producto
    # @method_decorator(csrf_exempt)
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)

    # def ingresoFactura(self, request):
    #     print(request.body)

    pass


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
