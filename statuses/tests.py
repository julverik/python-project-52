from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Status

User = get_user_model()

class StatusCRUDTest(TestCase):
    """Тесты для CRUD со статусами"""
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.force_login(self.user)
    
    def test_status_list(self):
        """Тест: список статусов доступен авторизованному пользователю"""
        response = self.client.get(reverse('statuses:statuses'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'statuses/statuses.html')
    
    def test_status_creation(self):
        """Тест: создание статуса"""
        data = {'name': 'Новый статус'}
        response = self.client.post(reverse('statuses:create'), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Status.objects.filter(name='Новый статус').exists())
    
    def test_status_update(self):
        """Тест: обновление статуса"""
        status = Status.objects.create(name='Старый статус')
        data = {'name': 'Новый статус'}
        response = self.client.post(
            reverse('statuses:update', args=[status.id]),
            data
        )
        self.assertEqual(response.status_code, 302)
        status.refresh_from_db()
        self.assertEqual(status.name, 'Новый статус')
    
    def test_status_delete(self):
        """Тест: удаление статуса"""
        status = Status.objects.create(name='Статус для удаления')
        response = self.client.post(
            reverse('statuses:delete', args=[status.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Status.objects.filter(id=status.id).exists())