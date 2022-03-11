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

    #todo: hacer el post para registro de usuario
    def post(self, request):
        data = json.loads(request.body)
        Persona.objects.create(nombre)
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
