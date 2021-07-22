from django import forms

from .models import Supplier


class SupplierCreateForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = "__all__"
        exclude =  ["created_by", "updated_by", 'slug', 'is_deleted']


class SupplierUpdateForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = "__all__"
        exclude = ["created_by", "updated_by", 'slug', 'is_deleted']
