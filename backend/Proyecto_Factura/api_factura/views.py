import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views import View
from .models import Persona

# Create your views here.


class RegistroCliente(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        jd = json.loads(request.body)
        Persona.objects.create(nombre=jd['nombre'], apellido=jd['apellido'], direccion=jd['direccion'], telefono=jd[
                               'telefono'], genero=jd['genero'], numero_identidad=jd['numero_identidad'])
        resp = {'mensaje': 'Acompletado'}
        return JsonResponse(resp)


#! aquiiii
#todo: terminar el buscar un usuario
def obtenerUsuario(request, id):
    usuario = Persona.objects.get(numero_identidad=id)
    print("aquii", usuario)
    datos = {'mensaje': 'completado'}
    return JsonResponse(usuario)


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
