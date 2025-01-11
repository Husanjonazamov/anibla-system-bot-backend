from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination

from ...models import AnimeModel, EpisodeModel


class AnimeEpisodeRetriveSerialzier(serializers.ModelSerializer):
    class Meta:
        model = EpisodeModel
        fields = [
            'pk',
            "index",
            "point",
        ]

    

class BaseAnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimeModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListAnimeSerializer(BaseAnimeSerializer):
    class Meta(BaseAnimeSerializer.Meta): ...


class RetrieveAnimeSerializer(serializers.ModelSerializer):
    episodes = serializers.SerializerMethodField()

    class Meta:
        model = AnimeModel
        exclude = [
            "created_at",
            "updated_at",
        ]

    def get_episodes(self, obj):
        request = self.context.get('request')
        queryset = obj.episodemodel_set.all().order_by('index')
        paginator = PageNumberPagination()
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        serializer = AnimeEpisodeRetriveSerialzier(
            paginated_queryset, many=True)
        return paginator.get_paginated_response(serializer.data).data


class CreateAnimeSerializer(BaseAnimeSerializer):
    class Meta(BaseAnimeSerializer.Meta): ...
