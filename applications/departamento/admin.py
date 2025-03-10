from django.contrib import admin
from .models import departamento

# Register your models here.

class departamento_admin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'shor_name',
        'anulate',
    )

admin.site.register(departamento,departamento_admin)