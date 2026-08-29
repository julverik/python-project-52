from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from statuses.models import Status
from labels.models import Label
from tasks.models import Task

User = get_user_model()

class TaskCRUDTest(TestCase):
    """Тесты для CRUD операций с задачами"""
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.status = Status.objects.create(name='Новый')
        self.client.force_login(self.user)
    
    def test_task_list(self):
        """Тест: список задач доступен авторизованному пользователю"""
        response = self.client.get(reverse('tasks:tasks'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/tasks.html')
    
    def test_task_creation(self):
        """Тест: создание задачи"""
        data = {
            'name': 'Новая задача',
            'description': 'Описание задачи',
            'status': self.status.id,
            'executor': self.user.id,
        }
        response = self.client.post(reverse('tasks:create'), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(name='Новая задача').exists())
    
    def test_task_update(self):
        """Тест: обновление задачи"""
        task = Task.objects.create(
            name='Старая задача',
            status=self.status,
            author=self.user
        )
        data = {
            'name': 'Обновленная задача',
            'status': self.status.id,
            'executor': self.user.id,
        }
        response = self.client.post(
            reverse('tasks:update', args=[task.id]),
            data
        )
        self.assertEqual(response.status_code, 302)
        task.refresh_from_db()
        self.assertEqual(task.name, 'Обновленная задача')
    
    def test_task_delete(self):
        """Тест: удаление задачи"""
        task = Task.objects.create(
            name='Задача для удаления',
            status=self.status,
            author=self.user
        )
        response = self.client.post(
            reverse('tasks:delete', args=[task.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(id=task.id).exists())
    
    def test_task_delete_permission_denied(self):
        """Тест: нельзя удалить чужую задачу"""
        other_user = User.objects.create_user(
            username='otheruser',
            password='testpass123'
        )
        task = Task.objects.create(
            name='Чужая задача',
            status=self.status,
            author=other_user
        )
        response = self.client.post(
            reverse('tasks:delete', args=[task.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(id=task.id).exists())


class TaskFilterTest(TestCase):
    """Тесты для фильтрации задач"""
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.other_user = User.objects.create_user(
            username='otheruser',
            password='testpass123'
        )
        self.status = Status.objects.create(name='Новый')
        self.label = Label.objects.create(name='Важная')
        self.client.force_login(self.user)
        
        self.task1 = Task.objects.create(
            name='Задача 1',
            status=self.status,
            author=self.user,
            executor=self.other_user
        )
        self.task1.labels.add(self.label)
        
        self.task2 = Task.objects.create(
            name='Задача 2',
            status=self.status,
            author=self.other_user,
            executor=self.user
        )
    
    def test_filter_by_status(self):
        """Тест: фильтрация по статусу"""
        response = self.client.get(
            reverse('tasks:tasks'),
            {'status': self.status.id}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Задача 1')
        self.assertContains(response, 'Задача 2')
    
    def test_filter_by_executor(self):
        """Тест: фильтрация по исполнителю"""
        response = self.client.get(
            reverse('tasks:tasks'),
            {'executor': self.other_user.id}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Задача 1')
        self.assertNotContains(response, 'Задача 2')
    
    def test_filter_by_label(self):
        """Тест: фильтрация по метке"""
        response = self.client.get(
            reverse('tasks:tasks'),
            {'labels': self.label.id}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Задача 1')
        self.assertNotContains(response, 'Задача 2')
    
    def test_filter_self_tasks(self):
        """Тест: фильтр 'Только свои задачи'"""
        response = self.client.get(
            reverse('tasks:tasks'),
            {'self_tasks': 'on'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Задача 1')
        self.assertNotContains(response, 'Задача 2')