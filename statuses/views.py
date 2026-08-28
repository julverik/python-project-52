from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Status
from .forms import StatusForm

class StatusListView(LoginRequiredMixin, ListView):
    """Список статусов"""
    model = Status
    template_name = 'statuses/statuses.html'
    context_object_name = 'statuses'
    login_url = 'users:login'

class StatusCreateView(LoginRequiredMixin, CreateView):
    """Создание статуса"""
    model = Status
    form_class = StatusForm
    template_name = 'statuses/create.html'
    success_url = reverse_lazy('statuses:statuses')
    login_url = 'users:login'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Статус успешно создан')
        return response

class StatusUpdateView(LoginRequiredMixin, UpdateView):
    """Редактирование статуса"""
    model = Status
    form_class = StatusForm
    template_name = 'statuses/update.html'
    success_url = reverse_lazy('statuses:statuses')
    login_url = 'users:login'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Статус успешно изменен')
        return response

class StatusDeleteView(LoginRequiredMixin, DeleteView):
    """Удаление статуса"""
    model = Status
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('statuses:statuses')
    login_url = 'users:login'

    def form_valid(self, form):
        if self.object.task_set.exists():
            messages.error(self.request, 'Невозможно удалить статус')
            return redirect('statuses:statuses')
        messages.success(self.request, 'Статус успешно удален')
        return super().form_valid(form)
