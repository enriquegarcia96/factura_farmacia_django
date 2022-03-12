from django.urls import path


from .views import FacturaView, RegistroCliente, Registro_categoria

# url de la aplicacion
urlpatterns = [
    path('registro/', RegistroCliente.as_view(), name='registro_cliente'),
    path('factura/', FacturaView.as_view(), name='factura_lista'),
    path('buscar/<str:id>', RegistroCliente.as_view(), name='buscar_usuario'),
    path('categoria', Registro_categoria.as_view(), name='categoria')
]
