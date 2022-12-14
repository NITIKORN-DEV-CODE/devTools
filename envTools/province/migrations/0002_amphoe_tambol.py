# Generated by Django 4.1.2 on 2022-10-06 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('province', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amphoe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aCode', models.IntegerField(default='0')),
                ('aName', models.CharField(default='', max_length=100)),
                ('pCode', models.IntegerField(default='0')),
                ('pName', models.CharField(default='', max_length=100)),
                ('createdDate', models.DateField(auto_now_add=True)),
                ('updateDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Tambol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tCode', models.IntegerField(default='0')),
                ('tName', models.CharField(default='', max_length=100)),
                ('aCode', models.IntegerField(default='0')),
                ('aName', models.CharField(default='', max_length=100)),
                ('pCode', models.IntegerField(default='0')),
                ('pName', models.CharField(default='', max_length=100)),
                ('createdDate', models.DateField(auto_now_add=True)),
                ('updateDate', models.DateField()),
            ],
        ),
    ]
