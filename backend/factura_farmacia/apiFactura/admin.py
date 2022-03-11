from django.contrib import admin


from .models import Persona, Factura, Categoria, Producto

# Register your models here.
admin.site.register(Persona)
admin.site.register(Factura)
admin.site.register(Categoria)
admin.site.register(Producto)
