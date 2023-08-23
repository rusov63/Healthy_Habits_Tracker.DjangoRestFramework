from django.core.management import BaseCommand
from users.models import User
import os

"""
Создание пользователя с флагом. if_staff = False
"""

class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='owner@mail.ru',
            name='owner',
            is_staff=False,
            is_superuser=False

        )

        user.set_password('123456')
        user.save()