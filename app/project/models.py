""" Модуль содержит классы моделей"""
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Feedback(models.Model):
    """ Класс модели обратной связи"""
    name = models.CharField(verbose_name="Ваше имя", max_length=30)
    number = PhoneNumberField(verbose_name="Ваш телефон",)
    email = models.EmailField(verbose_name="Ваш email", unique=True)

    def __str__(self):
        return f'Зарегистрирован {self.name}'
