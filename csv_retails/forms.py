
from django import forms
from .models import Fashion

class FashionForm(forms.ModelForm):
    class Meta:
        model = Fashion
        fields = '__all__'
        widgets = {
            'Date_Purchase': forms.DateInput(attrs={'type': 'date'}),
        }


class SearchForm(forms.Form):
    SEARCH_CHOICES = [
        ('Customer_Reference_ID', 'Customer Reference ID'),
        ('Item_Purchased', 'Item Purchased'),
        ('Purchase_Amount', 'Purchase Amount'),
        # ادامه...
    ]



    search_field = forms.ChoiceField(choices=[('', 'Select a field')] + SEARCH_CHOICES, required=False)
    search_term = forms.CharField(max_length=255, required=False)


class DeleteRowForm(forms.Form):
    row_id = forms.IntegerField(widget=forms.HiddenInput())