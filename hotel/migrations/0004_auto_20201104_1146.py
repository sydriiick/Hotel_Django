# Generated by Django 3.1.2 on 2020-11-04 03:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_auto_20201104_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Booking Date'),
        ),
    ]
