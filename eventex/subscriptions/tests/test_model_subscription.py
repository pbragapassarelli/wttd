from datetime import datetime

from django.shortcuts import resolve_url as r
from django.test import TestCase
from eventex.subscriptions.models import Subscription

class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Pedro',
            cpf='12345678901',
            email='teste@teste.com.br',
            phone='11 987654321'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created_at attribute."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Pedro', str(self.obj))

    def test_paid_default_to_False(self):
        """By default, paid must be False"""
        self.assertEqual(False, self.obj.paid)

    def test_get_absolute_url(self):
        url = r('subscriptions:detail', self.obj.pk)
        self.assertEqual(url, self.obj.get_absolute_url())