from unittest import TestCase
from test_db.models import TestData, Categories
from test_db.serializer import TestDataSerializer


class BookSerializerTestCase(TestCase):
    def test_ok(self):
        cat1 = Categories.objects.create(category='cat1')
        book1 = TestData.objects.create(title='Some city 1', text='This is some city description', cat_id=2)
        book2 = TestData.objects.create(title='Some city 2', text='This is some city description', cat_id=2)
        data = TestDataSerializer([book1, book2], many=True).data
        expected_data = [
            {
                'id': book1.id,
                'title': 'Some city 1',
                'text': 'This is some city description',
                'cat_id': 1
            },
            {
                'id': book2.id,
                'title': 'Some city 2',
                'text': 'This is some city description',
                'cat_id': 1
            }
        ]

        self.assertEqual(data, expected_data)
