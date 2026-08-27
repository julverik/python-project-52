from django.db import models
from django.utils import timezone

class Status(models.Model):
    """Модель статуса задачи"""
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Имя'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
        ordering = ['created_at']