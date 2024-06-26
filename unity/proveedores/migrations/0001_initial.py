# Generated by Django 5.0.6 on 2024-05-17 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_razon_social', models.CharField(max_length=100)),
                ('nit', models.CharField(max_length=20)),
                ('nombre_rep_legal', models.CharField(max_length=100)),
                ('identificacion', models.CharField(max_length=20)),
                ('telefono', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=255)),
                ('ciudad', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254)),
                ('opcion_persona', models.CharField(choices=[('1', 'Persona Natural'), ('2', 'Persona Jurídica')], max_length=1)),
            ],
        ),
    ]
