# Generated by Django 3.1.3 on 2020-11-20 02:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flyaway', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='fareType',
            field=models.CharField(choices=[('Partially Refundable', 'Partially Refundable'), ('Refundable', 'Refundable')], default=None, max_length=50),
        ),
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passengerName', models.CharField(max_length=50)),
                ('passengerGender', models.CharField(max_length=50)),
                ('passengerPhone', models.IntegerField()),
                ('passengerEmail', models.CharField(max_length=50)),
                ('passengerSeatNO', models.CharField(max_length=50)),
                ('transactionId', models.CharField(max_length=50)),
                ('bookingStatus', models.CharField(choices=[('Pending', 'Pending'), ('Not-Confirmed', 'Not-Confirmed'), ('Confirmed', 'Confirmed')], max_length=50)),
                ('PrimaryUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
