# Generated by Django 3.2.5 on 2021-07-23 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_order_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='uid',
            field=models.CharField(default='1EB1337B2224', editable=False, max_length=20),
        ),
    ]
