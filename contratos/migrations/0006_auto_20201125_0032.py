# Generated by Django 3.1.3 on 2020-11-25 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0005_remove_contrato_profit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='valorContrato',
            field=models.FloatField(blank=True, default=0, max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='valorGasto',
            field=models.FloatField(blank=True, default=0, max_length=45, null=True),
        ),
    ]
