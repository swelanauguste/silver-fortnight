from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from .models import Order
from .forms import OrderCreateForm, OrderUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


class OrderCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Order
    form_class = OrderCreateForm
    success_message = "%(product)s was created successfully"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class OrderUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Order
    form_class = OrderUpdateForm
    success_message = "%(product)s was updated successfully"
    template_name_suffix = '_update_form'

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    context_object_name = "order"



class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    context_object_name = "orders"

