# Generated by Django 5.1.6 on 2025-02-26 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='prueba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('subtitulo', models.CharField(blank=True, max_length=30)),
                ('cantidad', models.IntegerField(default=0, max_length=3)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
