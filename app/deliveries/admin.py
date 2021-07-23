from django.contrib import admin

from .models import Delivery

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ['product', 'uid', 'qty', 'delivery_date', 'deliveried_to']
