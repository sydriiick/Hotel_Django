# Generated by Django 3.1.2 on 2020-11-16 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20201104_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(auto_now=True, verbose_name='Last login'),
        ),
    ]
