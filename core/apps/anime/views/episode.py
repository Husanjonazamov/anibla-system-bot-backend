from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from ..models import EpisodeModel
from ..serializers.episode import CreateEpisodeSerializer, ListEpisodeSerializer, RetrieveEpisodeSerializer


@extend_schema(tags=["Episode"])
class EpisodeView(BaseViewSetMixin, ModelViewSet):
    queryset = EpisodeModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListEpisodeSerializer
            case "retrieve":
                return RetrieveEpisodeSerializer
            case "create":
                return CreateEpisodeSerializer
            case _:
                return ListEpisodeSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()
