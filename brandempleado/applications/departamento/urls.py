from django.urls import path
#importamos el archivo vistas
from . import views
#nombre que se le dio al paquete de urls y no tener que escribir toda la direccion
app_name = 'departamento_app'

urlpatterns = [
    path('new-departamento/',
         views.newdepartamentoview.as_view(),
         name='nuevo_departamento'
    ),
    path('lista-departamento/',
         views.departamentoListView.as_view(),
         name='lista_departamento'
    ),
]