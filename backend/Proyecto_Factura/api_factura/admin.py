from django.contrib import admin


from .models import Categoria, Descripcion_impuestos_descuentos, Factura, Factura_detalle, Persona, Producto

# Register your models here.
admin.site.register(Persona)
admin.site.register(Factura)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Factura_detalle)
admin.site.register(Descripcion_impuestos_descuentos)

