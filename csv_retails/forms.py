
from django import forms
from .models import Fashion

class FashionForm(forms.ModelForm):
    class Meta:
        model = Fashion
        fields = ['Customer_Reference_ID', 'Item_Purchased', 'Purchase_Amount', 'Review_Rating', 'Payment_Method']
