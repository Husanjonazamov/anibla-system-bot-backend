# Generated by Django 5.1.3 on 2025-01-11 13:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnimeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='Nomi')),
                ('uz_name', models.CharField(max_length=255, verbose_name='Uz Nomi')),
                ('shikimore_url', models.URLField(blank=True, null=True, verbose_name='shikimore_url')),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
            ],
            options={
                'verbose_name': 'AnimeModel',
                'verbose_name_plural': 'AnimeModels',
                'db_table': 'Anime',
            },
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.IntegerField(unique=True, verbose_name='user_id')),
                ('first_name', models.CharField(max_length=255, verbose_name='Ismi')),
                ('last_name', models.CharField(max_length=255, verbose_name='Familiyasi')),
                ('stage_name', models.CharField(max_length=255, verbose_name='Tahallusi')),
                ('phone', models.CharField(max_length=255, verbose_name='Telefon raqami')),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='balance')),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('rejissyor', 'Rejissyor'), ('tarjimon', 'Tarjimon'), ('ovoz aktyori', 'Ovoz aktyori'), ('timer', 'Timer')], max_length=255, verbose_name='role')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'UserModel',
                'verbose_name_plural': 'UserModels',
                'db_table': 'User',
            },
        ),
        migrations.CreateModel(
            name='EpisodeModel',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('index', models.AutoField(primary_key=True, serialize=False, verbose_name='index')),
                ('point', models.CharField(choices=[('translating', 'Tarjima qilish jarayonida'), ('voiceover', 'Ovoz berish jarayonida'), ('timing', 'Timing qilish jarayonida'), ('finished', 'Tugatilgan')], max_length=50, verbose_name='point')),
                ('target_file_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='target_file_id')),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anime.animemodel', verbose_name='anime')),
                ('timer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='timing_episodes', to='anime.usermodel')),
                ('translator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='translated_episodes', to='anime.usermodel')),
                ('voice_actors', models.ManyToManyField(blank=True, related_name='voiceover_episodes', to='anime.usermodel')),
            ],
            options={
                'verbose_name': 'EpisodeModel',
                'verbose_name_plural': 'EpisodeModels',
                'db_table': 'Episode',
            },
        ),
        migrations.AddField(
            model_name='animemodel',
            name='rejissor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Rejissor', to='anime.usermodel'),
        ),
    ]
