# Generated by Django 5.1.6 on 2025-02-26 03:49

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='habilidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(max_length=50, verbose_name='habilidad')),
            ],
            options={
                'verbose_name': 'habilidad',
                'verbose_name_plural': 'habilidades',
            },
        ),
        migrations.CreateModel(
            name='empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=50, verbose_name='Apellido')),
                ('full_name', models.CharField(blank=True, max_length=120, verbose_name='Nombre completo')),
                ('job', models.CharField(choices=[('0', 'Contador'), ('1', 'Administrador'), ('2', 'Economista'), ('3', 'Otros')], max_length=2, verbose_name='Cargo')),
                ('hoja_vida', ckeditor.fields.RichTextField(blank=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='empleado')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departamento.departamento')),
                ('habilidad', models.ManyToManyField(to='empleados.habilidad')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'ordering': ['id'],
                'unique_together': {('first_name', 'last_name')},
            },
        ),
    ]
