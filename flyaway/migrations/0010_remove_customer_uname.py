# Generated by Django 3.1.3 on 2020-11-24 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flyaway', '0009_customer_uname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='uname',
        ),
    ]
