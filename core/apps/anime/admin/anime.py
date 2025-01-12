from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import AnimeModel, EpisodeModel



class EpisodeInline(admin.TabularInline):
    model = EpisodeModel
    fields = ("index", "point", "translator",
              "voice_actors", "timer", "target_file_id")
    extra = 1
    show_change_link = True
    verbose_name = "Episode"
    verbose_name_plural = "Episodes"



@admin.register(AnimeModel)
class AnimeAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
    inlines = [EpisodeInline]
