from django.db import models
# Create your models here.


class Persona(models.Model):
    MASCULINO = 'M'
    FEMENINO = 'F'
    GENERO = [(MASCULINO, 'Masculino'), (FEMENINO, 'Femenino')]
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=8)
    genero = models.CharField(
        max_length=10, choices=GENERO, default='Masculino')
    numero_identidad = models.CharField(max_length=13)

    def __str__(self):
        return self.numero_identidad


class Factura(models.Model):
    fecha = models.DateField(auto_now=True)
    total = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    numeroIdentidad = models.ForeignKey(Persona, on_delete=models.CASCADE)

    def __str__(self):
        return self.numero_identidad


class Descripcion_impuesto_descuentos(models.Model):
    descripcion = models.CharField(max_length=30)
    valor = models.DecimalField(max_digits=3, decimal_places=2)
    estado = models.BooleanField(default=True, null=False)


class Descuentos(models.Model):
    descripcion_impuesto_descuentos_impuesto_descuento_id = models.ForeignKey(
        Descripcion_impuesto_descuentos, on_delete=models.CASCADE)


class Impuesto(models.Model):
    Descripcion_impuesto_descuentos_impuesto_descuentos_id = models.ForeignKey(
        Descripcion_impuesto_descuentos, models.CASCADE)


class Impuesto_por_factura(models.Model):
    impuesto_impuesto_id = models.ForeignKey(
        Impuesto, on_delete=models.CASCADE)
    factura_factura_id = models.ForeignKey(Factura, on_delete=models.CASCADE)


class factura_por_descuentos(models.Model):
    factura_factura_id = models.ForeignKey(Factura, on_delete=models.CASCADE)
    descuentos_descuentos_id = models.ForeignKey(
        Descuentos, on_delete=models.CASCADE)

    # todo esto esta malo
    def __str__(self):
        return self.factura_factura_id + self.descuentos_descuentos_id


categoria_status = [
    (1, 'Pastilla'),
    (2, 'Inyenccion'),
    (3, 'Jarabe'),
    (4, 'Analgésicos'),
    (5, 'Uso diario'),
]


class Categoria(models.Model):
    nombre = models.IntegerField(
        null=False, blank=False, choices=categoria_status)
    descripcion = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    precio_venta = models.DecimalField(max_digits=6, decimal_places=2)
    precio_costo = models.DecimalField(max_digits=6, decimal_places=2)
    nombre_producto = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    fecha_elaboracion = models.DateField(
        auto_now_add=False, null=True, blank=True)
    fecha_vencimiento = models.DateField(
        auto_now_add=False, null=True, blank=True)

    #  poner la categoria
    categoria_categoria_id = models.ForeignKey(
        Categoria, on_delete=models.CASCADE)


class Factura_detalle(models.Model):
    productos_productos_id = models.ForeignKey(
        Producto, on_delete=models.CASCADE)
    factura_factura_id = models.ForeignKey(Factura, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=3, decimal_places=2, null=True)
