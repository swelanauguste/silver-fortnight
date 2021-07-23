from django import forms

from .models import Delivery


class DeliveryCreateForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = "__all__"
        exclude = ["created_by", "updated_by"]
        widgets = {
            "delivery_date": forms.DateInput(attrs={"type": "date"}),
            "delivery_comment": forms.Textarea(attrs={"rows": 3}),
        }


class DeliveryUpdateForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = "__all__"
        exclude = ["created_by", "updated_by"]
        widgets = {
            "delivery_date": forms.DateInput(attrs={"type": "date"}),
            "delivery_comment": forms.Textarea(attrs={"rows": 3}),
        }
