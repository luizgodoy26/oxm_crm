# Generated by Django 3.1.3 on 2020-11-23 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contrato',
            name='dataIncusao',
        ),
    ]