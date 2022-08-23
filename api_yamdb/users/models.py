from django.contrib.auth.models import AbstractUser
from django.db import models


# id,username,email,role,bio,first_name,last_name
class User(AbstractUser):

    ROLES = (
        ('user','Зарегистрированный пользователь'),
        ('moderator','Модератор'),
        ('admin','Администратор'),
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
    role=models.CharField(
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
    first_name=models.CharField(
        max_length=30,
        blank=True,
        verbose_name='Имя' 
    )
    last_name=models.CharField(
        max_length=30,
        blank=True,
        verbose_name='Фамилия' 
    )
