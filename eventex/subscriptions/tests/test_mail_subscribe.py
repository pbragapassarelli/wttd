from django.test import TestCase
from django.core import mail


class SubscribePostValid(TestCase):

    def setUp(self):
        data = dict(
            name='Pedro',
            cpf='12345678901',
            email='teste@teste.com.br',
            phone='11 987654321' 
        )
        self.response = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expected = 'Confirmação de inscrição'
        self.assertEqual(expected, self.email.subject)

    def test_subscription_email_from(self):
        expected = 'contato@eventex.com.br'
        self.assertEqual(expected, self.email.from_email)

    def test_subscription_email_to(self):
        expected = ['contato@eventex.com.br', 'teste@teste.com.br']
        self.assertEqual(expected, self.email.to)

    def test_subscription_email_body(self):

        contents = [
            'Pedro',
            '12345678901',
            '11 987654321',
            'teste@teste.com.br'
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)