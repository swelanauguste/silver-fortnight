from django.db import models
from mixins.assets import TimeStampMixin
from django.urls import reverse
from django.utils.text import slugify
from suppliers.models import Supplier


class Category(TimeStampMixin):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(TimeStampMixin):
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.SET_NULL, null=True
    )
    supplier = models.ForeignKey(
        Supplier, related_name="product_suppliers", on_delete=models.SET_NULL, null=True
    )
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, null=True, unique=True)
    tags = models.TextField(
        blank=True, null=True, help_text="Tags separated by comma eg.: #tag, #tags"
    )
    image = models.ImageField(upload_to="products/", blank=True)
    description = models.TextField(blank=True)
    init_qty = models.IntegerField("initial quantity", default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"slug": self.slug})

    def get_update_url(self):
        return reverse("products:product-update", kwargs={"slug": self.slug})

    def get_order_balance(self):
        return sum(
            (order.get_order_quantity() for order in self.orders.all()), self.init_qty
        )
        # ) - (sum(item.get_delivered_quantity() for item in self.delivered_goods.all()))

    def get_delivered_balance(self):
        return sum(
            delivery.get_delivered_quantity() for delivery in self.deliveries.all()
        )

    def get_inventory_balance(self):
        return self.get_order_balance() - self.get_delivered_balance()

    def __str__(self):
        return self.name
