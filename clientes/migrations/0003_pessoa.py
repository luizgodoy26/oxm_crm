# Generated by Django 3.1.3 on 2020-11-18 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20201117_1936'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('codigo', models.IntegerField()),
                ('identificador', models.BigIntegerField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=45, null=True)),
                ('telefone', models.BigIntegerField(blank=True, null=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotos_clientes')),
            ],
        ),
    ]
