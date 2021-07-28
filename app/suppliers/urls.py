from django.urls import path

from . import views

app_name = "suppliers"

urlpatterns = [
    path("", views.SupplierListView.as_view(), name="supplier-list"),
    path("search/", views.SupplierSearch.as_view(), name="supplier-search"),
    path(
        "detail/<slug:slug>", views.SupplierDetailView.as_view(), name="supplier-detail"
    ),
    path("create", views.SupplierCreateView.as_view(), name="supplier-create"),
    path(
        "update/<slug:slug>", views.SupplierUpdateView.as_view(), name="supplier-update"
    ),
]
