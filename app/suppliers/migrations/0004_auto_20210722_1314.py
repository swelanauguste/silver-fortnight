# Generated by Django 3.2.5 on 2021-07-22 17:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('suppliers', '0003_auto_20210722_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='district',
            field=models.CharField(choices=[('gros_islet', 'Gros Islet'), ('castries', 'Castries'), ('soufriere', 'Soufriere'), ('vieux_fort', 'Vieux Fort')], default='castries', max_length=25),
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('created_by', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tags_created', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tags_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='supplier',
            name='tag',
            field=models.ManyToManyField(blank=True, to='suppliers.Tags'),
        ),
    ]
