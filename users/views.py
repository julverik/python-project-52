from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views import View
from django.contrib.auth import logout as auth_logout
from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm

class UserListView(ListView):
    model = User
    template_name = 'users/users.html'
    context_object_name = 'users'

class UserCreateView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('users:login')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Пользователь успешно зарегистрирован')
        return response

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users:users')
    
    def dispatch(self, request, *args, **kwargs):
        if self.get_object().id != request.user.id:
            messages.error(request, 'У вас нет прав для изменения')
            return redirect('users:users')
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Пользователь успешно изменен')
        return response

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users:users')
    
    def dispatch(self, request, *args, **kwargs):
        if self.get_object().id != request.user.id:
            messages.error(request, 'У вас нет прав для удаления')
            return redirect('users:users')
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        if User.objects.count() == 1:
            messages.error(self.request, 'Нельзя удалить последнего пользователя')
            return redirect('users:users')
        return super().form_valid(form)
    
    def get_success_url(self):
        messages.success(self.request, 'Пользователь успешно удален')
        return reverse_lazy('users:users')

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Вы залогинены')
        return response

class LogoutView(View):
    def post(self, request):
        auth_logout(request)
        messages.success(request, 'Вы разлогинены')
        return redirect('index')