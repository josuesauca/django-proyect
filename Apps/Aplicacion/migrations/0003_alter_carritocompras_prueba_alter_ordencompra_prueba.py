# Generated by Django 4.0.6 on 2022-07-09 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion', '0002_administrador_carritocompras_cliente_factura_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carritocompras',
            name='prueba',
            field=models.DecimalField(decimal_places=0, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='prueba',
            field=models.DecimalField(decimal_places=0, max_digits=7, null=True),
        ),
    ]