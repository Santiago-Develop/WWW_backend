# Generated by Django 4.2 on 2023-04-29 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Ciudad',
                'verbose_name_plural': 'Ciudades',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ciudad')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('cliente_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cliente')),
            ],
            options={
                'verbose_name': 'Sucursal',
                'verbose_name_plural': 'Sucursales',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Mensajero',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('cliente_id', models.ManyToManyField(to='app.cliente')),
            ],
            options={
                'verbose_name': 'Mensajero',
                'verbose_name_plural': 'Mensajeros',
                'ordering': ['nombre'],
            },
        ),
    ]