from django.test import TestCase
from .models import User
# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        user1 = User.objects.create(username = "Test_user",password = "123",email = "test123@google.cl")
        user2 = User.objects.create(username= "Test_user2",password = "829018901", email = "test123452@google.cl")
        return (user1,user2)

    def test_users_are_valid_instance(self):
        users = self.setUp()
        self.assertTrue(isinstance(users[0],User))
        self.assertTrue(isinstance(users[1],User))
