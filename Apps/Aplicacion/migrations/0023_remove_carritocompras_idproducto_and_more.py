# Generated by Django 4.0.6 on 2023-01-02 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion', '0022_remove_carritocompras_idcarritoproducto_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carritocompras',
            name='idProducto',
        ),
        migrations.AddField(
            model_name='carritocompras',
            name='productos',
            field=models.ManyToManyField(null=True, to='Aplicacion.producto'),
        ),
    ]
