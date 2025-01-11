from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class EpisodeModel(AbstractBaseModel):
    POINT_CHOICES = (
        ("translating", "Tarjima qilish jarayonida"),
        ("voiceover", "Ovoz berish jarayonida"),
        ("timing", "Timing qilish jarayonida"),
        ("finished", "Tugatilgan"),
    )

    anime = models.ForeignKey(
        "AnimeModel", on_delete=models.CASCADE, verbose_name=_("anime")
    )
    index = models.AutoField(_("index"), primary_key=True)
    point = models.CharField(_("point"), max_length=50, choices=POINT_CHOICES)

    translator = models.ForeignKey(
        "UserModel", on_delete=models.SET_NULL, null=True, blank=True, related_name="translated_episodes"
    )
    voice_actors = models.ManyToManyField(
        "UserModel", blank=True, related_name="voiceover_episodes"
    )
    timer = models.ForeignKey(
        "UserModel", on_delete=models.SET_NULL, null=True, blank=True, related_name="timing_episodes"
    )

    target_file_id = models.CharField(
        _("target_file_id"), max_length=255, blank=True, null=True)


    def __str__(self):
        return f"Episode {self.index}"

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "Episode"
        verbose_name = _("EpisodeModel")
        verbose_name_plural = _("EpisodeModels")
