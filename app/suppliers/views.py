from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Supplier
from .forms import SupplierCreateForm, SupplierUpdateForm


class SupplierListView(LoginRequiredMixin, ListView):
    model = Supplier
    context_object_name = "suppliers"
    paginate_by = 10


class SupplierDetailView(LoginRequiredMixin, DetailView):
    model = Supplier
    context_object_name = "supplier"


class SupplierCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Supplier
    form_class = SupplierCreateForm
    success_message = "%(name)s was created successfully"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated = self.request.user
        return super().form_valid(form)


class SupplierUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Supplier
    form_class = SupplierUpdateForm
    template_name_suffix = "_update_form"
    success_message = "%(name)s was updated successfully"

    def form_valid(self, form):
        form.instance.updated = self.request.user
        return super().form_valid(form)
