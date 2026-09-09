import django_filters
from django import forms
from django.contrib.auth import get_user_model

from labels.models import Label
from statuses.models import Status

from .models import Task

User = get_user_model()


class TaskFilter(django_filters.FilterSet):
    """Фильтр для задач"""

    status = django_filters.ModelChoiceFilter(
        queryset=Status.objects.all(),
        label="Статус",
        widget=forms.Select(
            attrs={
                "class": "w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
            }
        ),
    )

    executor = django_filters.ModelChoiceFilter(
        queryset=User.objects.all(),
        label="Исполнитель",
        widget=forms.Select(
            attrs={
                "class": "w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
            }
        ),
    )

    labels = django_filters.ModelChoiceFilter(
        queryset=Label.objects.all(),
        label="Метка",
        widget=forms.Select(
            attrs={
                "class": "w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
            }
        ),
    )

    self_tasks = django_filters.BooleanFilter(
        label="Только свои задачи",
        method="filter_self_tasks",
        widget=forms.CheckboxInput(
            attrs={
                "class": "w-4 h-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
            }
        ),
    )

    def filter_self_tasks(self, queryset, name, value):
        """Фильтр для отображения только задач автора"""
        if value:
            user = self.request.user
            return queryset.filter(author=user)
        return queryset

    class Meta:
        model = Task
        fields = ["status", "executor", "labels"]
