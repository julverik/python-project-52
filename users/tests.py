from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class UserCRUDTest(TestCase):
    """Тесты для CRUD операций с пользователями"""
    
    def setUp(self):
        """Создаем тестового пользователя"""
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
            first_name='Test',
            last_name='User'
        )
    
    def test_user_registration(self):
        """Тест регистрации пользователя"""
        data = {
            'first_name': 'New',
            'last_name': 'User',
            'username': 'newuser',
            'password1': 'testpass123',
            'password2': 'testpass123',
        }
        response = self.client.post(reverse('users:create'), data)
        self.assertEqual(response.status_code, 302) 
        self.assertTrue(User.objects.filter(username='newuser').exists())
    
    def test_user_update(self):
        """Тест обновления пользователя"""
        self.client.force_login(self.user)
        
        data = {
            'first_name': 'Updated',
            'last_name': 'Name',
            'username': 'updateduser',
        }
        response = self.client.post(
            reverse('users:update', args=[self.user.id]),
            data
        )
        self.assertEqual(response.status_code, 302)  
        
        
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'Updated')
        self.assertEqual(self.user.last_name, 'Name')
        self.assertEqual(self.user.username, 'updateduser')


    def test_user_delete(self):
        """Тест удаления пользователя"""
        user_to_delete = User.objects.create_user(
            username='deleteuser',
            password='testpass123'
        )
        user_id = user_to_delete.id
    
        self.client.force_login(user_to_delete)
    
        response = self.client.post(
            reverse('users:delete', args=[user_id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(User.objects.filter(id=user_id).exists())
    
    def test_user_update_permission_denied(self):
        """Тест: нельзя изменить чужого пользователя"""
        other_user = User.objects.create_user(
            username='otheruser',
            password='testpass123'
        )
        self.client.force_login(self.user)
        
        response = self.client.get(
            reverse('users:update', args=[other_user.id])
        )
        self.assertEqual(response.status_code, 302)
    
    def test_user_delete_permission_denied(self):
        """Тест: нельзя удалить чужого пользователя"""
        other_user = User.objects.create_user(
            username='otheruser',
            password='testpass123'
        )
        self.client.force_login(self.user)
        
        response = self.client.get(
            reverse('users:delete', args=[other_user.id])
        )
        self.assertEqual(response.status_code, 302)
    
    def test_user_login(self):
        """Тест входа пользователя"""
        response = self.client.post(reverse('users:login'), {
            'username': 'testuser',
            'password': 'testpass123',
        })
        self.assertEqual(response.status_code, 302)
    
    def test_user_logout(self):
        """Тест выхода пользователя"""
        self.client.force_login(self.user)
        response = self.client.post(reverse('users:logout'))
        self.assertEqual(response.status_code, 302)


class UserListViewTest(TestCase):
    """Тесты для страницы списка пользователей"""
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
    
    def test_user_list_accessible(self):
        """Тест: список пользователей доступен без авторизации"""
        response = self.client.get(reverse('users:users'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/users.html')
    
    def test_user_list_contains_users(self):
        """Тест: список пользователей содержит пользователей"""
        response = self.client.get(reverse('users:users'))
        self.assertContains(response, 'testuser')