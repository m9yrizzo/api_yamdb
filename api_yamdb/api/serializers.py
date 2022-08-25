from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from reviews.models import Comment, Review
from users.models import User
from categories.models import Category, Genre, Title


class ConfirmationCodeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('username', 'email',)
        model = User


class JWTTokenSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'username', 'bio', 'email', 'role', 'first_name', 'last_name',
        )
        model = User


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
        fields = '__all__'
        model = Review


class CommentSerializer(serializers.ModelSerializer):
    # review = serializers.PrimaryKeyRelatedField(read_only=True, )
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        read_only_fields = ('review', )
        model = Comment
