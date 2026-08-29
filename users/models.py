from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Модель пользователя с расширенными полями"""

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
