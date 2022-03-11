from django.contrib import admin


from .models import Categoria,  Descuentos, Descripcion_impuesto_descuentos , factura_por_descuentos,  Impuesto, Impuesto_por_factura, Factura, Factura_detalle, Persona, Producto

# Register your models here.
admin.site.register(Persona)
admin.site.register(Factura)
admin.site.register(Descripcion_impuesto_descuentos)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Factura_detalle)
admin.site.register(Descuentos)
admin.site.register(factura_por_descuentos)
admin.site.register(Impuesto)
admin.site.register(Impuesto_por_factura)
