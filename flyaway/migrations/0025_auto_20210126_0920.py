# Generated by Django 3.1.3 on 2021-01-26 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flyaway', '0024_auto_20210126_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='flight_date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='bookings',
            name='flight_from',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='refrencebooking',
            name='flight_date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]