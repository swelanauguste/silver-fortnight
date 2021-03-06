from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView, TemplateView, UpdateView

from .forms import EmployeeUpdateForm
from .models import Employee


class EmployeeListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Employee
    context_object_name = "employees"
    paginate_by = 10

    def test_func(self):
        return self.request.user.employee.is_ag

    def handle_no_permission(self):
        """ Do whatever you want here if the user doesn't pass the test """
        messages.error(self.request, 'Only the AG and SEO have access to this page')
        return redirect('/')


class EmployeeDetailView(LoginRequiredMixin, DetailView):
    model = Employee
    context_object_name = "employee"


class EmployeeUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Employee
    form_class = EmployeeUpdateForm
    template_name_suffix = '_update_form'
    success_message = "Your employee profile was updated successfully"
    
