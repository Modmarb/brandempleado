from django import forms

class newdepartamentoform(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    departamento = forms.CharField(max_length=50)
    nombre_cortoshorname = forms.CharField(max_length=50)