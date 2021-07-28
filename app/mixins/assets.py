from django.conf import settings
from django.db import models
from django.views.generic import ListView, TemplateView

User = settings.AUTH_USER_MODEL

DISTRICT_LIST = [
    ("Gros Islet", "Gros Islet"),
    ("Castries", "Castries"),
    ("Soufriere", "Soufriere"),
    ("Vieux Fort", "Vieux Fort"),
]


    # def get_queryset(self):
    #     query = self.request.GET.get('q')
    #     if query:
    #         return Employee.objects.filter(Q(first_name__icontains=query) |
    #                                         Q(last_name__name__icontains=query)
    #                                         ).distinct()
    #     else:
    #         return ""




class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="%(class)s_created",
        default=1,
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="%(class)s_updated",
        default=1,
    )

    class Meta:
        abstract = True






class Index(TemplateView):
    template_name = "index.html"
