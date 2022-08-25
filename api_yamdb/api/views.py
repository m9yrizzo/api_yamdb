from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

from categories.models import Title
from reviews.models import Review
from .permissions import IsAuthorModerAdminOrReadOnly
from .serializers import (
    ReviewSerializer,
    CommentSerializer,
)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthorModerAdminOrReadOnly, ]
    pagination_class = LimitOffsetPagination

    def get_title_id(self):
        return get_object_or_404(Title, pk=self.kwargs.get('title_id'))

    def get_queryset(self):
        return self.get_title_id().reviews.all()

    def perform_create(self, serializer):
        title = self.get_title_id()
        serializer.save(author=self.request.user, title_id=title)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorModerAdminOrReadOnly, ]
    pagination_class = LimitOffsetPagination

    def get_review_id(self):
        return get_object_or_404(Review, pk=self.kwargs.get('review_id'))

    def get_queryset(self):
        return self.get_review_id().comments.all()

    def perform_create(self, serializer):
        review = self.get_review_id()
        serializer.save(author=self.request.user, review_id=review)
