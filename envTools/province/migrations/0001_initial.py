# Generated by Django 4.1.2 on 2022-10-06 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pCode', models.IntegerField(default='0')),
                ('pName', models.CharField(default='', max_length=100)),
                ('pZone', models.IntegerField(default='0')),
                ('createdDate', models.DateField(auto_now_add=True)),
                ('updateDate', models.DateField()),
            ],
        ),
    ]
