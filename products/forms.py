from django import forms
from products.models import Product

class ProductForm(forms.ModelForm):
        
    class Meta:
        model = Product
        fields = ["name", "category", "image"]