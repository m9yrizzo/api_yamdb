from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from rest_framework.relations import SlugRelatedField

from reviews.models import Comment, Review


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
