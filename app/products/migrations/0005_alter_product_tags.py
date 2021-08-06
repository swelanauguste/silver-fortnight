# Generated by Django 3.2.5 on 2021-08-04 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.TextField(blank=True, help_text='Tags separated by comma eg.: #tag, #tags', null=True),
        ),
    ]