from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    """Форма для регистрации пользователя"""

    first_name = forms.CharField(
        label='Имя',
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
        })
    )
    last_name = forms.CharField(
        label='Фамилия',
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
        })
    )
    username = forms.CharField(
        label='Имя пользователя',
        max_length=150,
        help_text='Обязательное поле. Не более 150 символов. Только буквы, цифры и символы @/./+/-/_.',
        widget=forms.TextInput(attrs={
            'class': 'w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
        })
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            'class': 'w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
        }),
        help_text='Ваш пароль должен содержать как минимум 3 символа.'
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput(attrs={
            'class': 'w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
        }),
        help_text='Для подтверждения введите, пожалуйста, пароль ещё раз.'
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Пароли не совпадают')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class CustomUserChangeForm(UserChangeForm):
    """Форма для редактирования пользователя"""

    password = None

    first_name = forms.CharField(
        label='Имя',
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
        })
    )
    last_name = forms.CharField(
        label='Фамилия',
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
        })
    )
    username = forms.CharField(
        label='Имя пользователя',
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
        })
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')