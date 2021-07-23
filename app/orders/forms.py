from django import forms

from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
        exclude = ["created_by", "updated_by"]
        widgets = {
            "received_date": forms.DateInput(attrs={"type": "date"}),
            "received_comment": forms.Textarea(attrs={"rows": 3}),
        }


class OrderUpdateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
        exclude = ["created_by", "updated_by"]
        widgets = {
            "received_date": forms.DateInput(attrs={"type": "date"}),
            "received_comment": forms.Textarea(attrs={"rows": 3}),
        }
