# Generated by Django 3.1.3 on 2021-02-15 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flyaway', '0032_auto_20210215_2140'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookings',
            old_name='dateCreated',
            new_name='date',
        ),
    ]
