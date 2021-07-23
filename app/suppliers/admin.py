from django.contrib import admin

from .models import Supplier, Tag


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "created_at", "updated_at"]
    prepopulated_fields = {
        "slug": ("name",),
    }


admin.site.register(Tag)