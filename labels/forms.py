from django import forms
from .models import Label

class LabelForm(forms.ModelForm):
    """Форма для создания и редактирования метки"""
    
    class Meta:
        model = Label
        fields = ['name']
        labels = {
            'name': 'Имя',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
            }),
        }