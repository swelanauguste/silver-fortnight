# Generated by Django 3.2.5 on 2021-07-23 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20210722_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='uid',
            field=models.CharField(default='15F678147A6C', editable=False, max_length=20, unique=True),
        ),
    ]
