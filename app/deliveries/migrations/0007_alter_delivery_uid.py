# Generated by Django 3.2.5 on 2021-07-24 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deliveries', '0006_alter_delivery_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='uid',
            field=models.CharField(default='73DDFE2CB1FB', editable=False, max_length=20),
        ),
    ]
