# Generated by Django 3.1.3 on 2020-12-18 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flyaway', '0019_auto_20201218_1001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookings',
            name='flightId',
        ),
        migrations.AddField(
            model_name='bookings',
            name='flightnumber',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]