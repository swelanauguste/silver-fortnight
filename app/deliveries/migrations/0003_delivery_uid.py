# Generated by Django 3.2.5 on 2021-07-23 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deliveries', '0002_auto_20210723_0826'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='uid',
            field=models.CharField(default='A0680A38383F', editable=False, max_length=20),
        ),
    ]
