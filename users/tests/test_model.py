from .test_setup import TestSetUp
from users.models import User
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

# models test
class UserModelTest(TestSetUp):

    def create_user(self):
        return User.objects.create(
            name = self.user_data['name'],
            email = self.user_data['email'],
            city = self.user_data["city"],
            gender = self.user_data["gender"],
            password = self.user_data['password'],
        )
    
    def get_user(self, email):
        try:
            return User.objects.get(email=email)
        except ObjectDoesNotExist:
            return None
    
    def delete_user(self, user):
        return user.delete()

    def test_user_creation(self):
        user_created = self.create_user()
        self.assertTrue(isinstance(user_created, User))
        self.assertEqual(user_created.email, self.user_data['email'])
        self.assertEqual(user_created.name, self.user_data['name'])
        self.assertEqual(user_created.city, self.user_data['city'])
        self.assertEqual(user_created.gender, self.user_data['gender'])

        user_retrieved = self.get_user(user_created.email)
        self.assertTrue(isinstance(user_created, User))
        self.assertEqual(user_retrieved.email, self.user_data['email'])
        self.assertEqual(user_retrieved.name, self.user_data['name'])
        self.assertEqual(user_retrieved.city, self.user_data['city'])
        self.assertEqual(user_retrieved.gender, self.user_data['gender'])

        user_deleted = self.delete_user(user_retrieved)
        self.assertIsNone(self.get_user(user_created.email))
    
    