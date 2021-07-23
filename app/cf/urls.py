from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from mixins.assets import Index

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("suppliers/", include("suppliers.urls", namespace="suppliers")),
    path("products/", include("products.urls", namespace="products")),
    path("orders/", include("orders.urls", namespace="orders")),
    path("deliveries/", include("deliveries.urls", namespace="deliveries")),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
