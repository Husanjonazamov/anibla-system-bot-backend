from django_filters import rest_framework as filters

from ..models import EpisodeModel


class EpisodeFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = EpisodeModel
        fields = ("name",)
