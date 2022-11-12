from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from test_db.models import TestData, Categories
from test_db.serializer import TestDataSerializer


class BooksApiTestCase(APITestCase):
    def test_get(self):
        user = User.objects.create(username="username")
        book1 = TestData.objects.create(title='Some city 1', text='This is some city description', cat_id=1, population=1000000, mayor=user)
        book2 = TestData.objects.create(title='Some city 2', text='This is some city description', cat_id=1, population=456123, mayor=user)
        cat1 = Categories.objects.create(category='cat1')
        url = reverse('testdata-list')
        response = self.client.get(url)
        serializer_data = TestDataSerializer([book1, book2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
        print(TestData.objects.last().mayor)


class BookApiRelationTestCase(APITestCase):
    def setUp(self) -> None:
        self.user1 = User.objects.create(username='test_user1')
        self.user2 = User.objects.create(username='test_user2')
        self.book_1 = TestData.objects.create(title='some', text='sometexzt', cat=1, population=1000)

    def test_get(self):
        url = reverse('testdatarelation-detail')
        response = self.client.patch(url)
        serializer_data = TestDataSerializer




