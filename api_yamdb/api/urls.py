from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework.routers import DefaultRouter


router_v1 = DefaultRouter()


urlpatterns = [
    path('v1/auth/signup', get_confirmation_code.as_view()),
    path('v1/auth/token', get_jwt_token.as_view())
    path('v1/', include(router_v1.urls)),
]

