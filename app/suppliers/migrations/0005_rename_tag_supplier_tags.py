# Generated by Django 3.2.5 on 2021-08-04 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0004_alter_supplier_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supplier',
            old_name='tag',
            new_name='tags',
        ),
    ]
