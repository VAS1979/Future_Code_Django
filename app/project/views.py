"""
Модуль представлений приложения 'project'
"""
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import FeedbackCreateForm
from .utils import DataMixin, menu


class ProjectHome(DataMixin, TemplateView):
    """Класс представление
    главной страницы сайта"""
    template_name = 'project/index.html'
    title_page = 'Главная страница'


def contact(request):
    '''Функция представление
    страницы сайта "Обратная связь"'''
    if request.method == 'POST':
        form = FeedbackCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'project/register_done.html', {'title': 'Успешная регистрация', 'menu': menu})
    else:
        form = FeedbackCreateForm()

    data = {
        'title': 'Обратная связь',
        'menu': menu,
        'form': form,
        }
    return render(request, 'project/contact.html', data)


class ProjectAbout(DataMixin, TemplateView):
    """Класс представление
    страницы сайта <О нас>"""
    template_name = 'project/about.html'
    title_page = 'О нас'


def register_done(request):
    '''Функция представление
    страницы сайта "Успешная регистрация"'''

    data = {
        'title': 'Успешная регистрация',
        'menu': menu,
        }
    return render(request, 'project/register_done.html', data)
