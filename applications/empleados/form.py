from django import forms
from .models import empleado

class empleadoForm(forms.ModelForm):
    """Form definition for empleado."""

    class Meta:
        """Meta definition for empleadoform."""

        model = empleado
        fields = (
            'first_name',
            'last_name',
            'job',
            'departamento',
            'habilidad',
            'avatar',
        )
        widgets = {
            'habilidad': forms.CheckboxSelectMultiple()
        }
