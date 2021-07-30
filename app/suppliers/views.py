from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    TemplateView,
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy

from .models import Supplier
from .forms import SupplierCreateForm, SupplierUpdateForm, SupplierDeleteForm
from products.models import Product
from employees.models import Employee


class SupplierSearch(LoginRequiredMixin, ListView):
    model = Supplier
    template_name = "suppliers/supplier_search.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get("q")
        if query:
            suppliers = Supplier.objects.filter(
                Q(name__icontains=query)
                | Q(tag__name__icontains=query)
                | Q(description__icontains=query)
                | Q(email__icontains=query)
                | Q(phone__icontains=query)
                | Q(address__icontains=query)
                | Q(district__icontains=query)
            ).distinct()
            context["suppliers"] = suppliers
        else:
            context["suppliers"] = Supplier.objects.all()
        return context


class SupplierListView(LoginRequiredMixin, SuccessMessageMixin, FormMixin, ListView):
    model = Supplier
    form_class = SupplierCreateForm
    queryset = Supplier.object_list.all()
    context_object_name = "suppliers"
    paginate_by = 10
    success_message = "%(name)s was created successfully"


class SupplierDetailView(LoginRequiredMixin, DetailView):
    model = Supplier
    context_object_name = "supplier"


class SupplierCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Supplier
    form_class = SupplierCreateForm
    success_message = "%(name)s was created successfully"
    success_url = reverse_lazy("suppliers:supplier-list")

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


class SupplierDeleteView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Supplier
    form_class = SupplierDeleteForm
    success_message = "Delete successfully"
    success_url = reverse_lazy("suppliers:supplier-list")

    def form_valid(self, form):
        form.instance.updated = self.request.user
        form.instance.is_deleted = True
        return super().form_valid(form)
