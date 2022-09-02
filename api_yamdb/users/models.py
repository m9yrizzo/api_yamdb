from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    user = 'user'
    moderator = 'moderator'
    admin = 'admin'

    ROLES = (
        (user, user),
        (moderator, moderator),
        (admin, admin),
    )

    username = models.CharField(
        max_length=25,
        unique=True,
        blank=False,
        null=False,
        verbose_name='Имя пользователя'
    )
    email = models.TextField(
        max_length=50,
        unique=True,
        verbose_name='Почта'
    )
    role = models.CharField(
        max_length=30,
        blank=True,
        choices=ROLES,
        default='user',
        verbose_name='Роль пользователя'
    )
    bio = models.TextField(
        max_length=450,
        blank=True,
        verbose_name='Биография'
    )

    first_name = models.CharField(
        max_length=30,
        blank=True,
        verbose_name='Имя'
    )

    last_name = models.CharField(
        max_length=30,
        blank=True,
        verbose_name='Фамилия'
    )

    @property
    def is_user(self):
        return self.role == self.user

    @property
    def is_moderator(self):
        return self.role == self.moderator

    @property
    def is_admin(self):
        return self.role == self.admin or self.is_superuser

    class Meta:
        ordering = ('username',)

    def __str__(self):
        return self.username
