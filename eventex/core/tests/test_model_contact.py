from django.test import TestCase
from django.core.exceptions import ValidationError
from eventex.core.models import Speaker, Contact


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Pedro', 
            slug='pedro',
            photo='http://hbn.link/hb-pic'
        )

    def test_email(self):
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.EMAIL,
            value='a@a.com'
        )

        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.PHONE,
            value='11-987654321'
        )

        self.assertTrue(Contact.objects.exists())

    def test_choices(self):
        """Contact kind should be limited to E or P"""
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(
            speaker=self.speaker,
            kind=Contact.EMAIL,
            value='a@a.com'
        )
        self.assertEqual('a@a.com', str(contact))