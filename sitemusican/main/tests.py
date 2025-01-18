from django.test import TestCase

class TestMusician(TestCase):

    def text_index(self):
        response = self.client.get('books')
        self.assertEquals(response.status_code, 200)
