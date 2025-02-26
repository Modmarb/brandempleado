from django.contrib import admin
from .models import empleado, habilidad

# Register your models here.

admin.site.register(habilidad)

class empleado_admin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'full_name',
        'job',
        'departamento',
        'hoja_vida',
    )

    def nombre_completo(self,obj):
    
        return obj.first_name + ' ' + obj.last_name

    #se crea un campo para filtrar por nombre en el admin
    search_fields = ('first_name',)
    #se crea una lista de filtros por cargo en el admin
    list_filter = ('job','habilidad',)
    #añadir un filtro en la relacion muchos a muchos
    filter_horizontal = ('habilidad',)

admin.site.register(empleado,empleado_admin)