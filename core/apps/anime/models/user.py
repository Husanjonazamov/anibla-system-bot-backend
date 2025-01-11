from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class UserModel(AbstractBaseModel):
    user_id = models.CharField(_("user_id"), unique=True)

    role_choice = (
        ("admin", "Admin"),
        ("rejissyor", "Rejissyor"),
        ("tarjimon", "Tarjimon"),
        ("ovoz aktyori", "Ovoz aktyori"),
        ("timer", "Timer"),
    )
    first_name = models.CharField(_("Ismi"), max_length=255)
    last_name = models.CharField(_("Familiyasi"), max_length=255)
    stage_name = models.CharField(_("Tahallusi"), max_length=255)
    phone = models.CharField(_("Telefon raqami"), max_length=255)
    balance = models.DecimalField(
        _("balance"), max_digits=10, decimal_places=2, default=0)
    role = models.CharField(_("role"), max_length=255, choices=role_choice)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "User"
        verbose_name = _("UserModel")
        verbose_name_plural = _("UserModels")
