from django.db import models

# Create your models here.

class prueba(models.Model):
    titulo = models.CharField(max_length=30)
    subtitulo = models.CharField(max_length=30, blank=True)
    cantidad = models.IntegerField(max_length=3, default=0)

    class Meta:
        ordering = ['id']