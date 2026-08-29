from django import forms
from .models import Task
from labels.models import Label

class TaskForm(forms.ModelForm):
    """Форма для создания и редактирования задачи"""
    
    labels = forms.ModelMultipleChoiceField(
        queryset=Label.objects.all(),
        required=False,
        label='Метки',
        widget=forms.SelectMultiple(attrs={
            'class': 'w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
        })
    )
    
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']
        labels = {
            'name': 'Имя',
            'description': 'Описание',
            'status': 'Статус',
            'executor': 'Исполнитель',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
                'rows': 5
            }),
            'status': forms.Select(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
            }),
            'executor': forms.Select(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
            }),
        }