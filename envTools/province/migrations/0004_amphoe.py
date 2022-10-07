# Generated by Django 4.1.2 on 2022-10-06 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('province', '0003_delete_amphoe_delete_tambol'),
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
    ]
