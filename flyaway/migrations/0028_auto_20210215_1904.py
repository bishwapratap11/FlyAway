# Generated by Django 3.1.3 on 2021-02-15 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flyaway', '0027_bookings_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='flight_time',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='bookings',
            name='pnr',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
