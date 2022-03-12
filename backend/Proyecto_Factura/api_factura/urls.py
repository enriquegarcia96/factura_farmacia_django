from django.urls import path


from .views import FacturaView, Registro_Producto, RegistroCliente, Registro_categoria,Factura_de_compra

# url de la aplicacion
urlpatterns = [
    path('registro', RegistroCliente.as_view(), name='registro_cliente'),
    path('factura', FacturaView.as_view(), name='factura_lista'),
    path('compra', Factura_de_compra.as_view(), name='compra'),
    path('buscar/<str:id>', RegistroCliente.as_view(), name='buscar_usuario'),
    path('categoria', Registro_categoria.as_view(), name='categoria_lista'),
    path('categoria/<int:id>', Registro_categoria.as_view(), name='categoria'),
    path('producto', Registro_Producto.as_view(), name='registro_producto')
]
