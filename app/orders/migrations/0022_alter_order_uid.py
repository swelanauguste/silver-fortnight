# Generated by Django 3.2.5 on 2021-07-24 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0021_alter_order_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='uid',
            field=models.CharField(default='8353D4224707', editable=False, max_length=20),
        ),
    ]
