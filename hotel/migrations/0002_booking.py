# Generated by Django 3.1.2 on 2020-10-29 16:41

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateTimeField(verbose_name='Check In')),
                ('check_out', models.DateTimeField(verbose_name='Check Out')),
                ('booking_date', models.DateTimeField(default=datetime.datetime(2020, 10, 29, 16, 41, 6, 306357, tzinfo=utc), verbose_name='Booking Date')),
                ('booking_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.room', verbose_name='Room Number')),
                ('booking_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User ID')),
            ],
        ),
    ]
