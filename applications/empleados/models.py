from django.db import models
from applications.departamento.models import departamento
from ckeditor.fields import RichTextField

# Create your models here.

#se crea modelo habilidades
class habilidad(models.Model):
    habilidad = models.CharField('habilidad',max_length=50)

    class Meta:
        verbose_name = 'habilidad'
        verbose_name_plural = 'habilidades'

    def __str__(self):
        return self.habilidad
        
#se crea el modelo empleado
class empleado(models.Model):

    #se crea una lista con las opciones a seleccionr dentro del campo job
    job_choices = {
        '0':'Contador',
        '1':'Administrador',
        '2':'Economista',
        '3':'Otros',
    }

    #se crean los campos de la tabla
    first_name = models.CharField('Nombre',max_length=50)
    last_name = models.CharField('Apellido',max_length=50)
    full_name = models.CharField('Nombre completo',max_length=120,blank=True)# blank el campo no es obligatorio
    #el choices={variablelist} hace que este campo solo pueda tener esas opciones en una lista desplegable en el admin 
    job = models.CharField('Cargo',max_length=2,choices=job_choices)
    departamento = models.ForeignKey(departamento, on_delete=models.CASCADE)
    #image = models.ImageField(upload_to='empleado', blank=True, null=True)
    habilidad = models.ManyToManyField(habilidad)
    #creamos una columna que va a guardar un texto muy grande, por ejemplo una hv
    hoja_vida = RichTextField(blank=True)
    avatar = models.ImageField(upload_to='empleado',blank=True, null=True)

    #clase donde se va a realizar ajustes al modelo
    class Meta:
        #nombre de la tabla en admin
        verbose_name = 'Empleado'
        #nombre de la tabla en plural en admin
        verbose_name_plural = 'Empleados'
        #ordena de menor a mayor el nombre en admin
        ordering = ['id']
        #evita que se cree un registro igual en esta combinacion de columnas
        unique_together = ['first_name','last_name']


    #configura este modelo para que aparezca en admin
    def __str__(self):
        return str(self.id) + ' - ' + self.first_name + ' ' + self.last_name