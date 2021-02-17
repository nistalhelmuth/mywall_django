import json

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
        self.client.post("/users/register/", self.user_data)
        response = self.client.post(
            "/users/login/", 
            json.dumps({
                'email': self.user_data["email"],
                "password": self.user_data["password"]
            }), 
            content_type='application/json'
        )
        self.token = response.data["token"].decode("utf-8") 

        self.post_data = {
            'content': self.fake.text(),
        }

        self.comment_data = {
            'content': self.fake.text(),
        }
        return super().setUp()
    
    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer %s" % (self.token))

    def tearDown(self):
        return super().tearDown()