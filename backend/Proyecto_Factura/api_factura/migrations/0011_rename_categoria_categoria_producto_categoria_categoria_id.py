# Generated by Django 4.0.3 on 2022-03-13 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_factura', '0010_rename_categoria_categoria_id_producto_categoria_categoria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='categoria_categoria',
            new_name='categoria_categoria_id',
        ),
    ]
