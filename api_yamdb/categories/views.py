from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Avg
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import exceptions, filters, viewsets
from rest_framework.pagination import PageNumberPagination

from api.filters import TitleFilter
from api.permissions import IsAdmin, ReadOnlyPermission
from api.serializers import (CategorySerializer, GenreSerializer,
                             TitleSerializer)
from categories.models import Category, Genre, Title


class CategoryGenreViewSet(viewsets.ModelViewSet):
    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        try:
            obj = queryset.get(**filter_kwargs)
            return obj
        except ObjectDoesNotExist:
            raise exceptions.MethodNotAllowed(method='GET')


class CategoryViewSet(CategoryGenreViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    permission_classes = [IsAdmin | ReadOnlyPermission, ]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    pagination_class = PageNumberPagination


class GenreViewSet(CategoryGenreViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = 'slug'
    permission_classes = [IsAdmin | ReadOnlyPermission, ]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    pagination_class = PageNumberPagination


class TitleViewSet(viewsets.ModelViewSet):
    serializer_class = TitleSerializer
    permission_classes = [IsAdmin | ReadOnlyPermission, ]
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_class = TitleFilter
    search_fields = ('name',)
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return Title.objects.annotate(rating=Avg('reviews__score')).order_by(
            'name'
        )
