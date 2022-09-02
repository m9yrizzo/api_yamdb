from django.db import models

from api.validators import validate_year


class Genre(models.Model):
    name = models.CharField(
        max_length=128,
        verbose_name='Жанр'
    )
    slug = models.SlugField(
        max_length=64,
        verbose_name='Слаг жанра',
        unique=True
    )

    class Meta:
        verbose_name = 'Genre'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        max_length=128,
        verbose_name='Категория'
    )
    slug = models.SlugField(
        max_length=64,
        verbose_name='Слаг категории',
        unique=True
    )

    class Meta:
        verbose_name = 'Category'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(
        max_length=128,
        verbose_name='Произведение'
    )
    year = models.IntegerField(
        verbose_name='Год создания',
        db_index=True,
        validators=[validate_year]
    )
    description = models.TextField(
        verbose_name='Описание произведения',
        blank=True,
        null=True
    )
    genre = models.ManyToManyField(
        Genre,
        through='TitleGenre',
        verbose_name='Жанр произведения'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='title',
        verbose_name='Категория произведения',
        null=True,
    )

    class Meta:
        verbose_name = 'Title'
        ordering = ('-year',)

    def __str__(self):
        return self.name


class TitleGenre(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.SET_NULL,
        verbose_name='Произведение',
        null=True,
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.SET_NULL,
        verbose_name='Жанр произведения',
        null=True,
    )

    def __str__(self):
        return f'{self.genre} {self.title}'
