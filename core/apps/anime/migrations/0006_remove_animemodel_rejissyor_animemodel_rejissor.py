# Generated by Django 5.1.3 on 2025-01-12 13:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0005_remove_animemodel_rejissor_animemodel_rejissyor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animemodel',
            name='rejissyor',
        ),
        migrations.AddField(
            model_name='animemodel',
            name='rejissor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Rejissor', to='anime.usermodel'),
        ),
    ]
