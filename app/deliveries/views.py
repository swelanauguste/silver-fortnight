from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from .models import Delivery
from .forms import DeliveryCreateForm, DeliveryUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


class DeliveryCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Delivery
    form_class = DeliveryCreateForm
    success_message = "%(product)s was created successfully"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class DeliveryUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Delivery
    form_class = DeliveryUpdateForm
    success_message = "%(product)s was updated successfully"
    template_name_suffix = '_update_form'

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class DeliveryDetailView(LoginRequiredMixin, DetailView):
    model = Delivery
    context_object_name = "delivery"



class DeliveryListView(LoginRequiredMixin, ListView):
    model = Delivery
    context_object_name = "deliveries"

