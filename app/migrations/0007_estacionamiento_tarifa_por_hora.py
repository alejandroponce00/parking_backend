# Generated by Django 4.2.19 on 2025-03-11 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_estacionamiento_cupon_gratis_estacionamiento_tarifa'),
    ]

    operations = [
        migrations.AddField(
            model_name='estacionamiento',
            name='tarifa_por_hora',
            field=models.DecimalField(decimal_places=2, default=2.0, help_text='Tarifa base por hora en dólares', max_digits=5),
        ),
    ]
