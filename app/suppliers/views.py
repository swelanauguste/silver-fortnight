from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin

from .models import Supplier
from .forms import SupplierCreateForm, SupplierUpdateForm


class SupplierListView(ListView):
    model = Supplier


class SupplierDetailView(DetailView):
    model = Supplier


class SupplierCreateView(SuccessMessageMixin, CreateView):
    model = Supplier
    form_class = SupplierCreateForm
    success_message = "%(name)s was created successfully"

    # fields = ["name", "address", "phone", "email", "district", "website", "is_active"]


class SupplierUpdateView(SuccessMessageMixin, UpdateView):
    model = Supplier
    form_class = SupplierUpdateForm
    template_name_suffix = "_update_form"
    success_message = "%(name)s was updated successfully"
    # fields = ["name", "address", "phone", "email", "district", "website", "is_active"]
