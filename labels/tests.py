from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Label

User = get_user_model()


class LabelCRUDTest(TestCase):
    """Тесты для CRUD операций с метками"""

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpass123"
        )
        self.client.force_login(self.user)

    def test_label_list(self):
        """Тест: список меток доступен авторизованному пользователю"""
        response = self.client.get(reverse("labels:labels"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "labels/labels.html")

    def test_label_creation(self):
        """Тест: создание метки"""
        data = {"name": "Новая метка"}
        response = self.client.post(reverse("labels:create"), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Label.objects.filter(name="Новая метка").exists())

    def test_label_update(self):
        """Тест: обновление метки"""
        label = Label.objects.create(name="Старая метка")
        data = {"name": "Новая метка"}
        response = self.client.post(reverse("labels:update", args=[label.id]), data)
        self.assertEqual(response.status_code, 302)
        label.refresh_from_db()
        self.assertEqual(label.name, "Новая метка")

    def test_label_delete(self):
        """Тест: удаление метки"""
        label = Label.objects.create(name="Метка для удаления")
        response = self.client.post(reverse("labels:delete", args=[label.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Label.objects.filter(id=label.id).exists())
