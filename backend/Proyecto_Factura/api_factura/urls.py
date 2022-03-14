from django.urls import path


from .views import FacturaView, Registro_Producto, RegistroCliente, Registro_categoria, Factura_de_compra, Descripcion_impuesto

# url de la aplicacion
urlpatterns = [
    path('registro', RegistroCliente.as_view(), name='registro_cliente'),
    path('buscar/<int:id>', RegistroCliente.as_view(), name='buscar_usuario'),

    path('factura', FacturaView.as_view(), name='factura_lista'),
    path('compra/<int:id>', Factura_de_compra.as_view(), name='compra'),
    
    path('categoria', Registro_categoria.as_view(), name='categoria_lista'),
    path('categoria/<int:id>', Registro_categoria.as_view(), name='categoria'),
    path('producto', Registro_Producto.as_view(), name='registro_producto'),


    # descripcion impuestos descuentos
    path('descripcion_impuesto', Descripcion_impuesto.as_view(),
         name='impuesto_descripcion'),
    

]
