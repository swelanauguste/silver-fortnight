from django.urls import path

from . import views

app_name = "products"

urlpatterns = [
    path("", views.ProductListView.as_view(), name="product-list"),
    path("search/", views.ProductSearchListView.as_view(), name="product-search"),
    path("detail/<slug:slug>", views.ProductDetailView.as_view(), name="product-detail"),
    path("create", views.ProductCreateView.as_view(), name="product-create"),
    path("update/<slug:slug>", views.ProductUpdateView.as_view(), name="product-update"),
]
