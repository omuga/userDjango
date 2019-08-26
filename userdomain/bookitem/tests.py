from django.test import TestCase
from .models import Bookitem

class BookItemTestCase(TestCase):
    def setUp(self):
        book1 = Bookitem.objects.create(titulo = "Test_user1",descripcion = "123", author ="Test User")
        book2 = Bookitem.objects.create(titulo= "Test_user2", descripcion = "test_description", author = "TestUser1")
        return (book1,book2)

    def test_bookitem_if_valid_instance(self):
        books = self.setUp()
        self.assertTrue(isinstance(books[0],Bookitem))
        self.assertTrue(isinstance(books[1],Bookitem))



# Create your tests here.
