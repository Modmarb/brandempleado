from django.db import models

# Create your models here.

#crea el modelo departamento (tabla dentro de la base de datos)
class departamento(models.Model):
    #espesifica cada uno de los campos de la tabla
    name = models.CharField('Nombre', max_length=50)
    shor_name = models.CharField('Nombre_Corto',max_length=20)
    anulate = models.BooleanField('Anulado',default=False)

    class Meta:
        #nombre del modelo en admin
        verbose_name = 'Departamento'
        #nombre del modelo plural en admin
        verbose_name_plural = 'Departamentos'
        #ordernar de nemor a mayor en la tabla del admin
        ordering = ['name']
        #evita que se registre de nuevo una combinacion de name y shor_name
        unique_together = ['name','shor_name']

    #configura el admin para que este modelo aparezca
    def __str__(self):
        return self.name
