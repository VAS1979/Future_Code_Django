"""
Модуль содержит словарь меню сайта и базовый класс DataMixin
"""
menu = [{'title': "Обратная связь", 'url_name': "contact"},
        {'title': "О нас", 'url_name': "about"},
        ]


class DataMixin:
    """Класс для расширения функционала классов
    представлений и наполнения общей информацией"""
    title_page = None
    extra_context = {}

    def __init__(self) -> None:
        if self.title_page:
            self.extra_context['title'] = self.title_page

        if 'menu' not in self.extra_context:
            self.extra_context['menu'] = menu

    def get_mixin_context(self, context, **kwargs):
        """Функция возвращает словарь с меню сайта"""
        context['menu'] = menu
        return context
