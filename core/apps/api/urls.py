from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.apps.anime.views import UserView, EpisodeView, AnimeView

router = DefaultRouter()

router.register(r"user", UserView, basename="user")
router.register(r"anime", AnimeView, basename="anime")
router.register(r"episode", EpisodeView, basename="episode")


urlpatterns = [
    path("", include(router.urls)),
]
