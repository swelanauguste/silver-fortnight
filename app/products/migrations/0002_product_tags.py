# Generated by Django 3.2.5 on 2021-07-22 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0002_auto_20210722_1744'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='product_tags', to='suppliers.Tag'),
        ),
    ]