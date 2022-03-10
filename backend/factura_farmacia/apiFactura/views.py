from django.http import JsonResponse
from django.views import View

from .models import Persona

# Create your views here.


class FacturaView(View):

    def get(slef, request):
        companies = list(Persona.objects.values())
        if len(companies) > 0:
            datos = {'mensaje': 'completado', 'compañias': companies}
        else: 
            datos = {'mensaje': 'error' }
        return JsonResponse(datos)
