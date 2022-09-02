from django.core import validators
from django.db import models

from categories.models import Title
from users.models import User


class Review(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(
        verbose_name='Дата добавления',
        auto_now_add=True,
        db_index=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews')
    score = models.PositiveSmallIntegerField(
        validators=[
            validators.MaxValueValidator(
                10,
                message='Максимальная оценка должна быть не более 10'
            ),
            validators.MinValueValidator(
                1,
                message='Минимальная оценка должна быть не менее 1'
            ),
        ]
    )
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='reviews')

    class Meta:
        ordering = ['pub_date']
        constraints = (
            models.UniqueConstraint(
                fields=('title', 'author',),
                name='unique_review',
            ),
        )

    def __str__(self):
        return self.text


class Comment(models.Model):
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    pub_date = models.DateTimeField(
        verbose_name='Дата добавления',
        auto_now_add=True,
        db_index=True)

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return self.text
