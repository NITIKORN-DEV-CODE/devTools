# Generated by Django 4.1.2 on 2022-10-10 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ImageProduct',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
