from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .forms import newdepartamentoform
from applications.empleados.models import empleado
from .models import departamento

#Create your views here.


class departamentoListView(ListView):
    model = departamento
    template_name = "departamento/lista.html"
    context_object_name='departamentos'


class newdepartamentoview(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = newdepartamentoform
    success_url = '/'

    def form_valid(self, form):
        print('**************estamos en el form valid************')

        depa = departamento(
            name = form.cleaned_data['departamento'],
            shor_name = form.cleaned_data['nombre_cortoshorname']
        )
        depa.save()

        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']
        empleado.objects.create(
            first_name = nombre,
            last_name = apellido,
            job = '1',
            departamento = depa
        )
        return super(newdepartamentoview, self).form_valid(form)