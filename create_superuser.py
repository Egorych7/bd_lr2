from django.contrib.auth import get_user_model
from django.core.management import execute_from_command_line
import sys

# Установите переменную окружения DJANGO_SETTINGS_MODULE
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# Инициализируйте Django
import django
django.setup()

# Создайте суперпользователя
User = get_user_model()
if not User.objects.filter(username='Егор').exists():
    User.objects.create_superuser(
        username='Егор',
        email='vem161106@yandex.ru',
        password='bd234'
    )
    print("Суперпользователь 'Егор' создан.")
else:
    print("Суперпользователь 'Егор' уже существует.")