import json
from rest_framework import status
from .test_setup import TestSetUp
from users.models import User

class UsersTestCase(TestSetUp):
    def test_create_posts(self):
        self.api_authentication()
        response = self.client.post(
            "/posts/", 
            json.dumps({
                'content': self.post_data["content"],
            }), 
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["content"], self.post_data["content"])

    def test_list_posts(self):
        self.api_authentication()
        self.client.post(
            "/posts/", 
            json.dumps({
                'content': self.post_data["content"],
            }), 
            content_type='application/json'
        )
        response = self.client.get("/posts/", self.user_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["results"][0]["content"], self.post_data["content"])
    
    def test_create_comment(self):
        self.api_authentication()
        response = self.client.post(
            "/posts/", 
            json.dumps({
                'content': self.post_data["content"],
            }), 
            content_type='application/json'
        )
        response = self.client.post(
            "/posts/%d/"%(response.data["id"]), 
            json.dumps({
                'content': self.comment_data["content"],
            }), 
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["content"], self.comment_data["content"])
    
    def test_lists_comments(self):
        self.api_authentication()
        response = self.client.post(
            "/posts/", 
            json.dumps({
                'content': self.post_data["content"],
            }), 
            content_type='application/json'
        )
        self.client.post(
            "/posts/%d/"%(response.data["id"]), 
            json.dumps({
                'content': self.comment_data["content"],
            }), 
            content_type='application/json'
        )
        response = self.client.get("/posts/%d/"%(response.data["id"]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["content"], self.comment_data["content"])
