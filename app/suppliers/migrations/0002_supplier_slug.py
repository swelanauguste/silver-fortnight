# Generated by Django 3.2.5 on 2021-07-22 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='slug',
            field=models.SlugField(max_length=255, null=True, unique=True),
        ),
    ]
