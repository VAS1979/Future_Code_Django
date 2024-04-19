""" Модуль содержит формы"""
from django import forms
from .models import Feedback


class FeedbackCreateForm(forms.ModelForm):
    """
    Форма отправки обратной связи
    """
    class Meta:
        model = Feedback
        fields = ('name', 'number', 'email')
