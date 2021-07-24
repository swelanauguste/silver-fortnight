from django.contrib import admin

from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['product', 'qty', 'purchase_order_number', 'received_by']
