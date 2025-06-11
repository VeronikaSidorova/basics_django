from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'image',
            'category',
            'price',
            'created_at',
            'updated_at'
        ]
        widgets = {
            'created_at': forms.DateInput(attrs={'type': 'date'}),
            'updated_at': forms.DateInput(attrs={'type': 'date'}),
        }