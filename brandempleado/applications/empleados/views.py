from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic  import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from .form import empleadoForm

#models

from .models import empleado

# Create your views here.

class inicioview(TemplateView):
    """"vista que carga la pagina de inicio"""
    template_name = 'inicio.html'

#crear vista lista empleados totales
class list_all_empleados(ListView):
    #nombre el archivo html que va a llamar para mostrar los datos
    template_name = 'empleados/list_all.html'
    #pagina es decir que solo muestra el numero de datos que se establesca
    paginate_by = 10
    #modelo que se va a usar
    #model = empleado

    def get_queryset(self):
        print('***********************')
        palabra_clave = self.request.GET.get("kword",'')
        lista = empleado.objects.filter(
            first_name__icontains = palabra_clave
        )
        print(palabra_clave)
        
        return lista
    

class list_empleados_admin(ListView):
    template_name = 'empleados/list_empleados.html'
    paginate_by = 10
    model = empleado
    context_object_name='empleados'


#lista de empleados filtrados por departamento
class list_empleados_by_departamento(ListView):
    #nombre el archivo html que va a llamar para mostrar los datos
    template_name = 'empleados/list_by_departamento.html'
    context_object_name='empleados'
    paginate_by = 4

    #funcion para optener los datos desde el modelo e imprimirlos en el html
    def get_queryset(self):
        #se crea una variable que guarde lo optenido por el metodo GET
        departamento = self.kwargs['departamento']
        #nos conectamos al modelo empleado y filtramos por la variable deparamento de arriba
        lista = empleado.objects.filter(
            departamento__name = departamento
        )
        #retornamos los datos
        return lista

class listempleadosbykword(ListView):
    #lista empleados por palabra clave
    template_name = 'empleados/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",)
        lista = empleado.objects.filter(
            first_name = palabra_clave
        )
        print(palabra_clave)
        
        return lista
    
class lista_habilidades_empleado(ListView):
    template_name = 'empleados/listahabilidadempleado.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        #llega el campo empleado por get y se captura
        id_nombre = self.request.GET.get("empleado")
        #se retorta las habilidades de ese empleado, como es muchos a muchos se hace asi para retornar valores muchos a muchos se debe hacer seleccionando un solo empleado
        empleados = empleado.objects.get(id = id_nombre)
        lista = empleados.habilidad.all()
        return lista

#creamos una clase para desplegar un boton de detalle
class EmpleadoDetailView(DetailView):
    model = empleado
    template_name = "empleados/detail_empleado.html"
    #con esta funcion podemos enviar mas variables al html
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        #con esto podemos enviar varias variables al html, debemos crear una lista
        #context['titulo1'] = 'Titulo 1'
        #context['titulo2'] = 'Titulo 2'
        print(context)

        return context
    
#clase para registrar datos en el servidor
class empleadoCreateView(CreateView):
    model = empleado
    template_name = "empleados/create_empleado.html"
    #debemos espesificar que campos se van a llenar, en este caso escogemos todos
    form_class = empleadoForm
    # fields = [
    #     'first_name',
    #     'last_name',
    #     'job',
    #     'departamento',
    #     'habilidad'
    #]
    #este parametro nos dice despues de agregar los datos a donde va a redireccionar, debemos espesificar la url en este caso usamos el paquete reverse_lazy el cual nos permite poner una url por el nombre y no por la url, empleados_app es el nombre del paquete de url de personas y correcto es el nombre de la url
    success_url = reverse_lazy('empleados_app:empleados_admin')

    #con esta funcion podemos hacer algun otro proceso cuando el form sea valido, es decir cuando el form pueda ingresar los datos se ejecuta esto que esta dentro de la funcion
    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(empleadoCreateView, self).form_valid(form)

#clase de django para traer un html sencillo
class successview(TemplateView):
    template_name = "empleados/successview.html"


#clase para actualizar informacion de la base de datos
class empleadoUpdateView(UpdateView):
    model = empleado
    template_name = "empleados/update.html"
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidad'
    ]

    success_url = reverse_lazy('empleados_app:empleados_admin')
    #funcion para intersectar el post, quiere decir intersectar antes de que se validen los datos para cargar
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('*********************************')
        print(request.POST)

        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(empleadoUpdateView, self).form_valid(form)
    

class empleadoDeleteView(DeleteView):
    model = empleado
    template_name = "empleados/delete_empleado.html"
    success_url = reverse_lazy('empleados_app:empleados_admin')
