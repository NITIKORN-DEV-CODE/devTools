# Generated by Django 4.1.2 on 2022-10-07 05:19

from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgName', models.CharField(default='', max_length=100)),
                ('imgUrl', models.ImageField(blank=True, null=True, upload_to=product.models.upload_des)),
                ('prodId', models.IntegerField(default='0')),
                ('createdDate', models.DateField(auto_now_add=True)),
                ('updateDate', models.DateField()),
                ('stat', models.CharField(default='A', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prodName', models.CharField(default='', max_length=100)),
                ('prodDetail', models.CharField(default='', max_length=250)),
                ('prodPrice', models.IntegerField(default='0')),
                ('createdDate', models.DateField(auto_now_add=True)),
                ('updateDate', models.DateField()),
                ('stat', models.CharField(default='A', max_length=1)),
            ],
        ),
    ]