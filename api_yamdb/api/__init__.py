from django.urls import include, path
from rest_framework.routers import SimpleRouter

from categories.views import CategoryViewSet, GenreViewSet, TitleViewSet

router = SimpleRouter()

router.register(r'genres', GenreViewSet, basename='genres')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'titles', TitleViewSet, basename='titles')

urlpatterns = [
    path('v1/', include(router.urls)),
]
