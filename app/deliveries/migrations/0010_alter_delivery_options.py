# Generated by Django 3.2.5 on 2021-07-30 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deliveries', '0009_remove_delivery_uid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='delivery',
            options={'ordering': ['-created_at'], 'verbose_name_plural': 'Deliveries'},
        ),
    ]
