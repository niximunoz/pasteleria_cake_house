# Generated by Django 3.1.2 on 2021-06-16 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20210614_1250'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='codigo_de_Barras',
            new_name='id',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='fecha_de_Ingreso',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='marca',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='precio_Costo',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='precio_Venta',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='stock',
        ),
    ]
