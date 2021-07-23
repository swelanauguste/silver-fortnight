import uuid
from django.db import models
from products.models import Product
from mixins.assets import TimeStampMixin
from django.urls import reverse


def purchase_order_path(instance, filename):
    return "purchase_orders/%s/%s" % (instance.pk, filename)


def uid():
    uid = uuid.uuid4()
    uid = str(uid).upper()
    return uid.split("-")[4]


class Order(TimeStampMixin):
    uid = models.CharField(max_length=20, editable=False, default=uid())
    product = models.ForeignKey(
        Product, related_name="orders", on_delete=models.SET_NULL, null=True
    )
    qty = models.IntegerField(default=0)
    received_date = models.DateField(blank=True, null=True)
    received_by = models.CharField(max_length=100, blank=True, null=True)
    received_from = models.CharField(max_length=100, blank=True, null=True)
    received_comment = models.TextField(blank=True, null=True)
    purchase_order_number = models.CharField(max_length=100, blank=True, null=True)
    purchase_order = models.FileField(
        blank=True, null=True, upload_to=purchase_order_path
    )

    def get_absolute_url(self):
        return reverse("orders:order-detail", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("orders:order-update", kwargs={"pk": self.pk})

    def get_order_quantity(self):
        return self.qty

    def __str__(self):
        return self.product.name
