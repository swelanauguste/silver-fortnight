# Generated by Django 3.2.5 on 2021-08-04 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0003_auto_20210804_0556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='tag',
            field=models.TextField(blank=True, help_text='Tags separated by comma eg.: #tag, #tags', null=True),
        ),
    ]
