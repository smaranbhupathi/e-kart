# Generated by Django 4.0.1 on 2022-05-22 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0004_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='phone',
            field=models.CharField(default='', max_length=111),
        ),
    ]
