# Generated by Django 4.2 on 2023-07-18 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_alter_orderdetails_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdetails',
            name='image',
        ),
    ]
