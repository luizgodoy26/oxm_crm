# Generated by Django 3.1.3 on 2020-11-24 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0003_auto_20201123_0026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contrato',
            name='codigo',
        ),
    ]
