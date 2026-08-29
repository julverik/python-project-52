from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Label
from .forms import LabelForm

class LabelListView(LoginRequiredMixin, ListView):
    """Список меток"""
    model = Label
    template_name = 'labels/labels.html'
    context_object_name = 'labels'
    login_url = 'users:login'

class LabelCreateView(LoginRequiredMixin, CreateView):
    """Создание метки"""
    model = Label
    form_class = LabelForm
    template_name = 'labels/create.html'
    success_url = reverse_lazy('labels:labels')
    login_url = 'users:login'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Метка успешно создана')
        return response

class LabelUpdateView(LoginRequiredMixin, UpdateView):
    """Редактирование метки"""
    model = Label
    form_class = LabelForm
    template_name = 'labels/update.html'
    success_url = reverse_lazy('labels:labels')
    login_url = 'users:login'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Метка успешно изменена')
        return response

class LabelDeleteView(LoginRequiredMixin, DeleteView):
    """Удаление метки"""
    model = Label
    template_name = 'labels/delete.html'
    success_url = reverse_lazy('labels:labels')
    login_url = 'users:login'
    
    def form_valid(self, form):
        if self.object.task_set.exists():
            messages.error(self.request, 'Невозможно удалить метку')
            return redirect('labels:labels')
        messages.success(self.request, 'Метка успешно удалена')
        return super().form_valid(form)