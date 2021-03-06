from django.db import models

from django.urls import reverse

from django.conf import settings

Employee = settings.AUTH_USER_MODEL
from mixins.assets import TimeStampMixin


class Position(TimeStampMixin):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Department(TimeStampMixin):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.SET_NULL, null=True)
    # employment_id = models.CharField(max_length=10, unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    # middle_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    tel = models.CharField(max_length=25, null=True, blank=True)
    position = models.ForeignKey(
        Position, on_delete=models.SET_NULL, null=True, blank=True
    )
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, null=True, blank=True
    )
    is_seo = models.BooleanField("SEO", default=False)
    is_ag = models.BooleanField("AG", default=False)

    def get_absolute_url(self):
        return reverse("employees:employee-detail", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("employees:employee-update", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["last_name", "first_name"]
    
    def get_employee_initials(self):
        if self.first_name and self.last_name:
            return ("%s%s" % (self.first_name[0], self.last_name[0])).upper()
        return (self.employee.username[0]).upper()

    def get_full_name(self):
        if self.first_name and self.last_name:
            return "%s, %s" % (self.last_name, self.first_name)
        return self.employee.username

    def get_user_email(self):
        return self.employee.email

    def __str__(self):
        return self.employee.username
