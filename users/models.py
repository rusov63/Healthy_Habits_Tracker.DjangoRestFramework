from django.contrib.auth.models import AbstractUser
from django.db import models

from habit.models import NULLABLE


class User(AbstractUser):
    """
    Класс модель описывающее Пользователя.
    Авторизация и регистрация через e-mail
    """
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    name = models.CharField(max_length=200, verbose_name='Фамилия Имя Отчество', **NULLABLE)
    phone = models.CharField(max_length=37, verbose_name='Телефон', **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='Город', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватарка', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Добавить пользователя'
        verbose_name_plural = 'все пользователи'
        ordering = ('email',)