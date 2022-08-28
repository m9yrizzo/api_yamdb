from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from rest_framework.relations import SlugRelatedField
from reviews.models import Comment, Review
from users.models import User
from categories.models import Category, Genre, Title


class ConfirmationCodeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('username', 'email',)
        model = User


class JWTTokenSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    confirmation_code = serializers.CharField(required=True)
    class Meta:
        fields = (
            'username', 'confirmation_code',
        )
        model = User


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'username', 'bio', 'email', 'role', 'first_name', 'last_name',
        )
        model = User
    def validate_role(self, value):
        user = self.context['request'].user
        if user.role == 'user' and value == 'admin':
            value = 'user'
        return value


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug',)
        lookup_field = 'slug'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name', 'slug',)
        lookup_field = 'slug'


class TitleSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Genre.objects.all(),
        many=True,
        required=True,
    )
    category = serializers.SlugRelatedField(
        slug_field='slug', queryset=Category.objects.all(), required=True
    )
    rating = serializers.IntegerField(required=False)

    class Meta:
        model = Title
        fields = (
            'id',
            'name',
            'year',
            'description',
            'genre',
            'category',
            'rating',
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        genre_list = []
        for genre_data in data['genre']:
            genre = GenreSerializer(Genre.objects.get(slug=genre_data)).data
            genre_list.append(genre)
        data['genre'] = genre_list
        data['category'] = CategorySerializer(
            Category.objects.get(slug=data['category'])
        ).data
        return data


class ReviewSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Review
        fields = (
            'id', 'text', 'author', 'score', 'pub_date'
        )
        read_only_fields = ('id', 'author', 'pub_date')
        validators = (
            UniqueTogetherValidator(
                queryset=Review.objects.all(),
                fields=('title_id', 'author'),
                message=(
                    'Пользователь может оставить только'
                    'один отзыв на произведение!'
                )
            ),
        )

    def validate_score(self, value):
        if (value >= 1 and value <= 10):
            return value
        raise serializers.ValidationError(
            'Рэйтинг должен быть в диапазоне 1..10'
        )


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_date')
        read_only_fields = ('id', 'author', 'pub_date')
