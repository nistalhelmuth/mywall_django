from .test_setup import TestSetUp
from users.models import User
from django.utils import timezone

# models test
class UserModelTest(TestSetUp):

    def create_user(self):
        return User.objects.create(
            name = self.user_data['name'],
            email = self.user_data['email'],
            city = self.user_data["city"],
            genre = self.user_data["genre"],
            password = self.user_data['password'],
        )

    def test_user_creation(self):
        w = self.create_user()
        self.assertTrue(isinstance(w, User))
        self.assertEqual(w.email, self.user_data['email'])
        self.assertEqual(w.name, self.user_data['name'])
        self.assertEqual(w.city, self.user_data['city'])
        self.assertEqual(w.genre, self.user_data['genre'])
    
    