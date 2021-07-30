from django import forms

from .models import Supplier


class SupplierDeleteForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ["is_deleted"]


class SupplierCreateForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = "__all__"
        exclude = ["created_by", "updated_by", "slug", "is_deleted"]
        widgets = {"description": forms.Textarea(attrs={"rows": 3})}


class SupplierUpdateForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = "__all__"
        exclude = ["created_by", "updated_by", "slug", "is_deleted"]
        widgets = {"description": forms.Textarea(attrs={"rows": 3})}
