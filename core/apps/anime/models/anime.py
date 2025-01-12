from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from core.apps.anime.models.user import UserModel

class AnimeModel(AbstractBaseModel):
    name = models.CharField(_("Nomi"), max_length=255)
    uz_name = models.CharField(_("Uz Nomi"), max_length=255)
    shikimore_url = models.URLField(_("shikimore_url"), blank=True, null=True)
    rejissyor = models.ForeignKey(
        UserModel, on_delete=models.SET_NULL, related_name=_("Rejissor"),null=True)
    is_active = models.BooleanField(_("is_active"), default=True)

    def __str__(self):
        return self.name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "Anime"
        verbose_name = _("AnimeModel")
        verbose_name_plural = _("AnimeModels")
