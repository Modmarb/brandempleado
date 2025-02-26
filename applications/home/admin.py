from django.contrib import admin
from .models import prueba

# Register your models here.

class prueba_admin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = (
        'id',
        'titulo',
        'subtitulo',
        'cantidad',
    )

admin.site.register(prueba,prueba_admin)