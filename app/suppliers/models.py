from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from mixins.assets import DISTRICT_LIST, TimeStampMixin

# create a model manager filter
class IsNotDeletedManager(models.Manager):
    def get_queryset(self):
        return super(IsNotDeletedManager, self).get_queryset().filter(is_deleted=False)


# class Tag(TimeStampMixin):
#     name = models.CharField(max_length=100, blank=True, null=True)

#     class Meta:
#         ordering = ["name"]

#     def __str__(self):
#         return self.name


class Supplier(TimeStampMixin):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=255, null=True, unique=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    district = models.CharField(
        max_length=25, choices=DISTRICT_LIST, default="Castries"
    )
    website = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    tags = models.TextField(
        blank=True, null=True, help_text="Tags separated by comma eg.: #tag, #tags"
    )

    objects = models.Manager()
    object_list = IsNotDeletedManager()

    class Meta:
        ordering = ["name"]

    def get_delete_url(self):
        return reverse("suppliers:supplier-delete", kwargs={"slug": self.slug})

    def get_update_url(self):
        return reverse("suppliers:supplier-update", kwargs={"slug": self.slug})

    def get_absolute_url(self):
        return reverse("suppliers:supplier-detail", kwargs={"slug": self.slug})

    def get_full_address(self):
        return "%s, %s" % (self.address, self.district)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Supplier, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
