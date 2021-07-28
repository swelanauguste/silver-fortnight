from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product
from .forms import ProductCreateForm, ProductUpdateForm
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q


class ProductSearchListView(ListView):
    model = Product
    template_name = "products/product_search.html"
    context_object_name = "products"
    paginate_by = 10
    queryset = Product.objects.all()

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Product.objects.filter(
                Q(category_name__icontains=query)
                | Q(supplier_name__icontains=query)
                | Q(name__icontains=query)
                | Q(tags_name__icontains=query)
                | Q(description__icontains=query)
            )
        else:
            return Product.objects.all()


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    context_object_name = "products"
    paginate_by = 10


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    context_object_name = "product"


class ProductCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Product
    form_class = ProductCreateForm
    success_message = "%(name)s was created successfully"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Product
    form_class = ProductUpdateForm
    template_name_suffix = "_update_form"
    success_message = "%(name)s was updated successfully"

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)
