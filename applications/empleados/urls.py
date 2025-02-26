from django.urls import path
#importamos el archivo vistas
from . import views
#nombre que se le dio al paquete de urls y no tener que escribir toda la direccion
app_name = 'empleados_app'

urlpatterns = [
    path('', views.inicioview.as_view()),
    path('listar-todo-empleados/',
        views.list_all_empleados.as_view(),
        name='empleados_all'
    ),
    path('lista_empleados_admin/',
        views.list_empleados_admin.as_view(),
        name='empleados_admin'
    ),
    path('listar-by-departamento/<departamento>/',
         views.list_empleados_by_departamento.as_view(),
         name='empleados_departamento'
    ),
    path('buscar-empleado/', views.listempleadosbykword.as_view()),
    path('lista_habilidad_empleado/', views.lista_habilidades_empleado.as_view()),
    path('ver_empleado/<pk>/',
         views.EmpleadoDetailView.as_view(),
         name='empleado_detalle'
    ),
    path('crear_empleado/',
         views.empleadoCreateView.as_view(),
         name='crear_empleado'
    ),
    path(
        'successview/',
        views.successview.as_view(),
        name='correcto'
    ),
    path(
        'update_empleado/<pk>',
        views.empleadoUpdateView.as_view(),
        name='modificar_empleado'
    ),
    path(
        'delete_empleado/<pk>',
        views.empleadoDeleteView.as_view(),
        name='delete_empleado'
    ),
]