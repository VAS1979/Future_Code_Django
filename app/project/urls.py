"""
Модуль для определения URL-маршрутов приложения 'project'.
Содержит определение URL-маршрутов и их связь с представлениями (views).
"""
from django.urls import path
from .views import (ProjectHome, ProjectAbout, contact, register_done)


urlpatterns = [
    path('', ProjectHome.as_view(), name='home'),
    path('contact/', contact, name='contact'),
    path('about/', ProjectAbout.as_view(), name='about'),
    path('register_done/', register_done, name='register_done'),
]
