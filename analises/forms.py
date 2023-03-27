from django import forms

from .models import Analises




class CreateAnaliseForm(forms.ModelForm):
    
    class Meta:
        model = Analises
        fields = '__all__'
        widgets = {
            'data_inicio': forms.TextInput(attrs={'type': 'date','required': False}),
            'data_entrega': forms.TextInput(attrs={'type': 'date','required': False}),
        }
