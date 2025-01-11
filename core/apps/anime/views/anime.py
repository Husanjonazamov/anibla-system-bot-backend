from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from ..models import AnimeModel
from ..serializers.anime import CreateAnimeSerializer, ListAnimeSerializer, RetrieveAnimeSerializer


@extend_schema(tags=["Anime"])
class AnimeView(BaseViewSetMixin, ModelViewSet):
    queryset = AnimeModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListAnimeSerializer
            case "retrieve":
                return RetrieveAnimeSerializer
            case "create":
                return CreateAnimeSerializer
            case _:
                return ListAnimeSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()
