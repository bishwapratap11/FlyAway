# Generated by Django 3.1.3 on 2020-11-29 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flyaway', '0016_bookings_flightid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='passengerSeatNO',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
