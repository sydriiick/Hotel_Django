# Generated by Django 3.1.2 on 2020-11-13 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0010_auto_20201113_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_user',
            field=models.EmailField(max_length=50, verbose_name='Customer email'),
        ),
    ]
