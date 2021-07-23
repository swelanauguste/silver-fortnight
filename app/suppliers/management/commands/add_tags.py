from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from suppliers.models import Tag


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("file_name", type=str)

    def handle(self, *args, **kwargs):
        file_name = kwargs["file_name"]
        with open(f"{file_name}") as file:
            for row in file:
                name = row.lower().replace("\n", "")
                self.stdout.write(self.style.SUCCESS(f"{name} added"))
                updated_by = User.objects.get(pk=1)
                created_by = User.objects.get(pk=1)
                Tag.objects.get_or_create(
                    name=name, created_by=created_by, updated_by=updated_by
                )
        self.stdout.write(self.style.SUCCESS("list of objects added"))