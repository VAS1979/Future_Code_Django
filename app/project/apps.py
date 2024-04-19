"""
Модуль для конфигурации приложения "myapp".
Определяет конфигурацию и поведение приложения в рамках Django-проекта, включая
настройки, регистрацию сигналов и другие действия при инициализации приложения.
"""
from django.apps import AppConfig


class ProjectConfig(AppConfig):
    """
    Класс конфигурации приложения "myapp".
    Определяет конфигурацию и поведение приложения в рамках Django-проекта.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'project'
