# Generated by Django 4.0.3 on 2022-03-13 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_factura', '0009_alter_producto_categoria_categoria_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='categoria_categoria_id',
            new_name='categoria_categoria',
        ),
    ]
