# Generated by Django 4.1.6 on 2024-03-04 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_order_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='price',
        ),
    ]
