# Generated by Django 3.2.3 on 2021-07-04 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_rename_pastel_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='digito_verificador',
            field=models.IntegerField(choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7'], [8, '8'], [9, '9'], [10, 'K']]),
        ),
    ]