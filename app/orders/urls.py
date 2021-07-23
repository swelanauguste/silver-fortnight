from django.urls import path

from . import views

app_name = "orders"

urlpatterns = [
    path("", views.OrderListView.as_view(), name="order-list"),
    path("detail/<int:pk>", views.OrderDetailView.as_view(), name="order-detail"),
    path("update/<int:pk>", views.OrderUpdateView.as_view(), name="order-update"),
    path("create", views.OrderCreateView.as_view(), name="order-create"),
]
