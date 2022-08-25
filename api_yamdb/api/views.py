from django.shortcuts import render
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status, permissions

from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny, IsAuthenticated

from reviews.models import Review
from .serializers import ConfirmationCodeSerializer
from .permissions import IsAuthorModerAdminOrReadOnly
from .serializers import (
    ReviewSerializer,
    CommentSerializer,
)


@api_view(['POST'])
@permission_classes([AllowAny])
def get_confirmation_code(self,request):
#def post(self, request):
#    http_method_names = ['post', ]
#    permission_classes = (permissions.AllowAny,)

    serializer = ConfirmationCodeSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    email = serializer.validated_data['email']
    confirmation_code = default_token_generator.make_token(user)
    send_mail(
        'Регистрация', f'Код подтверждения: {confirmation_code}',
        'admin@yambd', [email], fail_silently=False, )
    return Response(serializer.validated_data, status=status.HTTP_200_OK)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthorModerAdminOrReadOnly, ]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        # serializer.save(author=self.request.user)
        pass


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorModerAdminOrReadOnly, ]

    def get_review_id(self):
        return get_object_or_404(Review, pk=self.kwargs.get('review_id'))

    def get_queryset(self):
        return self.get_review_id().comments.all()

    def perform_create(self, serializer):
        review = self.get_review_id()
        serializer.save(author=self.request.user, review=review)
