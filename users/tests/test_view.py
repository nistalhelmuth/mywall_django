import json
from rest_framework import status
from .test_setup import TestSetUp
from users.models import User

class UsersTestCase(TestSetUp):

    def test_registration(self):
        response = self.client.post("/users/register/", self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["email"], self.user_data["email"])

    def test_retrieve_profile(self):
        response = self.client.post("/users/register/", self.user_data)
        response = self.client.get("/users/profile/%d/" % (response.data["id"]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_authentication(self):
        self.client.post("/users/register/", self.user_data)
        response = self.client.post(
            "/users/login/", 
            json.dumps({
                'email': self.user_data["email"],
                "password": self.user_data["password"]
            }), 
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
   