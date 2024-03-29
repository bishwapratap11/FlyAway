# Generated by Django 3.1.3 on 2020-11-24 02:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flyaway', '0002_auto_20201120_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='PrimaryUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flyaway.customer'),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='bookingStatus',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Not-Confirmed', 'Not-Confirmed'), ('Confirmed', 'Confirmed')], default='Not-Confirmed', max_length=50),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='passengerGender',
            field=models.CharField(choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Others', 'Others')], max_length=50),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='transactionId',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
