from django.urls import path
from .views import FacturaView, RegistroCliente,obtenerUsuario

# url de la aplicacion
urlpatterns = [
    path('registro/', RegistroCliente.as_view(), name='registro_cliente'),
    path('factura/', FacturaView.as_view(), name='factura_lista'),
    path('buscar/<str:id>', obtenerUsuario )
]
