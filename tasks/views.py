from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
)
from django_filters.views import FilterView

from .filters import TaskFilter
from .forms import TaskForm
from .models import Task


class TaskListView(LoginRequiredMixin, FilterView):
    """Список задач с фильтрацией"""

    model = Task
    template_name = "tasks/tasks.html"
    context_object_name = "tasks"
    login_url = "users:login"
    filterset_class = TaskFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = self.filterset_class(
            self.request.GET, queryset=queryset, request=self.request
        )
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not hasattr(self, "filterset"):
            self.filterset = self.filterset_class(
                self.request.GET, queryset=self.get_queryset(), request=self.request
            )
        context["filter"] = self.filterset
        return context


class TaskDetailView(LoginRequiredMixin, DetailView):
    """Просмотр задачи"""

    model = Task
    template_name = "tasks/detail.html"
    context_object_name = "task"
    login_url = "users:login"


class TaskCreateView(LoginRequiredMixin, CreateView):
    """Создание задачи"""

    model = Task
    form_class = TaskForm
    template_name = "tasks/create.html"
    success_url = reverse_lazy("tasks:tasks")
    login_url = "users:login"

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, "Задача успешно создана")
        return response


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    """Редактирование задачи"""

    model = Task
    form_class = TaskForm
    template_name = "tasks/update.html"
    success_url = reverse_lazy("tasks:tasks")
    login_url = "users:login"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Задача успешно изменена")
        return response


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    """Удаление задачи"""

    model = Task
    template_name = "tasks/delete.html"
    success_url = reverse_lazy("tasks:tasks")
    login_url = "users:login"

    def dispatch(self, request, *args, **kwargs):
        task = self.get_object()
        if task.author != request.user:
            messages.error(request, "Задачу может удалить только ее автор")
            return redirect("tasks:tasks")
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        messages.success(self.request, "Задача успешно удалена")
        return reverse_lazy("tasks:tasks")
