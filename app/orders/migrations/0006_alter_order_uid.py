# Generated by Django 3.2.5 on 2021-07-23 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_order_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='uid',
            field=models.CharField(default='57BEA1B19CFB', editable=False, max_length=20),
        ),
    ]