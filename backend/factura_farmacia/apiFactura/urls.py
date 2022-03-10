from django.urls import path
from .views import FacturaView

#url de la aplicacion
urlpatterns = [
    path('factura/', FacturaView.as_view(), name='factura_lista')
]