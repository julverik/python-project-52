from django import forms

from .models import Status


class StatusForm(forms.ModelForm):
    """Форма для создания и редактирования статуса"""

    class Meta:
        model = Status
        fields = ["name"]
        labels = {
            "name": "Имя",
        }
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                }
            ),
        }
