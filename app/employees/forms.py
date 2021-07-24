from django import forms

from .models import Employee


class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ["first_name", "last_name", "tel", "department", "position"]


