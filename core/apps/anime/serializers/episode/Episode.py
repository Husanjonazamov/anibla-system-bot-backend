from rest_framework import serializers

from ...models import EpisodeModel


class BaseEpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EpisodeModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListEpisodeSerializer(BaseEpisodeSerializer):
    class Meta(BaseEpisodeSerializer.Meta): ...


class RetrieveEpisodeSerializer(BaseEpisodeSerializer):
    class Meta(BaseEpisodeSerializer.Meta): ...


class CreateEpisodeSerializer(BaseEpisodeSerializer):
    class Meta(BaseEpisodeSerializer.Meta): ...
