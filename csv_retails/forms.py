
from django import forms
from .models import Fashion

class FashionForm(forms.ModelForm):
    class Meta:
        model = Fashion
        fields = '__all__'
        widgets = {
            'Date_Purchase': forms.DateInput(attrs={'type': 'date'}),
        }