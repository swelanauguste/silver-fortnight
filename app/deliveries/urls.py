from django.urls import path

from . import views

app_name = "deliveries"

urlpatterns = [
    path("", views.DeliveryListView.as_view(), name="delivery-list"),
    path("detail/<int:pk>", views.DeliveryDetailView.as_view(), name="delivery-detail"),
    path("update/<int:pk>", views.DeliveryUpdateView.as_view(), name="delivery-update"),
    path("create", views.DeliveryCreateView.as_view(), name="delivery-create"),
]
