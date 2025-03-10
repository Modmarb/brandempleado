from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import prueba
from django.urls import reverse_lazy
from .forms import pruebaForm
# Create your views here.

class indexview(TemplateView):
    template_name = 'home/home.html'
    
class pruebalistview(ListView):
    template_name = 'home/list.html'
    queryset = ['A','B','C']
    context_object_name = 'lista_prueba'


class MODEL_pruebaListView(ListView):
    model = prueba
    template_name = "home/pruebas.html"
    context_object_name = 'lista_prueba'


class pruebaCreateView(CreateView):
    model = prueba
    template_name = "home/add.html"
    form_class = pruebaForm
    success_url = '/'


class resumenfoundationview(TemplateView):
    template_name = "home/resumenfoundationview.html"
