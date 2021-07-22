from django import forms

from .models import Product

class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ['slug', 'updated_by', 'created_by']
        widgets = {"description": forms.Textarea(attrs={"rows": 3})}


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ['slug', 'updated_by', 'created_by']
        widgets = {"description": forms.Textarea(attrs={"rows": 3})}