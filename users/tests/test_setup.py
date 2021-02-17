from rest_framework.test import APITestCase
from faker import Faker

from users.models import User

class TestSetUp(APITestCase):

    def setUp(self):
        self.fake = Faker()

        self.user_data = {
            'email': self.fake.email(),
            'name': self.fake.name(),
            "city": "Test City",
            "gender": "M",
            'password': self.fake.email(),
        }

        return super().setUp()
    
    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer %s" % (self.token))

    def tearDown(self):
        return super().tearDown()