from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework.routers import DefaultRouter
from categories.views import CategoryViewSet, GenreViewSet, TitleViewSet
from .views import get_confirmation_code

router_v1 = DefaultRouter()
router_v1.register(r'genres', GenreViewSet, basename='genres')
router_v1.register(r'categories', CategoryViewSet, basename='categories')
router_v1.register(r'titles', TitleViewSet, basename='titles')


urlpatterns = [
    path('v1/auth/signup', get_confirmation_code, name='signup'),
#    path('v1/auth/token', get_jwt_token.as_view())
    path('v1/', include(router_v1.urls)),
]
