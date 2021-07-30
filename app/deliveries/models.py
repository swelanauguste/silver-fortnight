import uuid
from django.db import models
from django.urls import reverse
from mixins.assets import TimeStampMixin
from products.models import Product

# def uid():
#     uid = uuid.uuid4()
#     uid = str(uid).upper()
#     return uid.split("-")[4]



# Create your models here.
class Delivery(TimeStampMixin):
    # uid = models.CharField(max_length=20, editable=False, default=uid())

    product = models.ForeignKey(
        Product, related_name="deliveries", on_delete=models.SET_NULL, null=True
    )
    qty = models.IntegerField(default=0)
    delivery_date = models.DateField(blank=True, null=True)
    deliveried_to = models.CharField(max_length=100, blank=True, null=True)
    deliveried_by = models.CharField(max_length=100, blank=True, null=True)
    delivery_comment = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Deliveries"

    def get_absolute_url(self):
        return reverse("deliveries:delivery-detail", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("stores:deliveries-update", kwargs={"pk": self.pk})

    def get_delivered_quantity(self):
        return self.qty

    def __str__(self):
        return self.product.name
