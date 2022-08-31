from django.urls import include, path
from rest_framework.routers import DefaultRouter

from categories.views import CategoryViewSet, GenreViewSet, TitleViewSet

from .views import (CommentViewSet, ReviewViewSet, UserView, UserViewSet,
                    get_confirmation_code, get_token)

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register('users', UserViewSet)
router_v1.register(r'titles', TitleViewSet, basename='titles')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)' r'/comments',
    CommentViewSet,
    basename='comments',
)
router_v1.register(r'genres', GenreViewSet, basename='genres')
router_v1.register(r'categories', CategoryViewSet, basename='categories')


urlpatterns = [
    path('v1/auth/signup/', get_confirmation_code),
    path('v1/auth/token/', get_token),
    path('v1/users/me/', UserView.as_view(), name='user_me'),
    path('v1/', include(router_v1.urls)),
]
