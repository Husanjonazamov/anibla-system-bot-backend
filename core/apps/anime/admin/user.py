from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import UserModel


@admin.register(UserModel)
class UserAdmin(ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "stage_name",
        "phone",
        "balance",
        "role",
    )
    readonly_fields = ("balance", )
    search_fields = ("first_name", "last_name", "stage_name", "phone")
    list_filter = ("role", "stage_name", "balance")
