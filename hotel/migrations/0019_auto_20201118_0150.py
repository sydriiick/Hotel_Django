# Generated by Django 3.1.2 on 2020-11-18 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0018_comment_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]