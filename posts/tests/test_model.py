from .test_setup import TestSetUp
from posts.models import Post, Comment
from users.models import User
from django.utils import timezone

# models test
class PostModelTest(TestSetUp):

    def create_post(self, user):
        return Post.objects.create(
            content = self.post_data['content'],
            created_by = user, 
        )

    def test_post_creation(self):
        user = User.objects.get(email = self.user_data['email'])
        post = self.create_post(user)
        self.assertTrue(isinstance(post, Post))
        self.assertEqual(post.content, self.post_data['content'])
    
class CommentModelTest(TestSetUp):

    def create_comment(self, user):
        return Comment.objects.create(
            content = self.comment_data['content'],
            created_by = user,
        )

    def test_user_creation(self):
        user = User.objects.get(email = self.user_data['email'])
        comment = self.create_comment(user)
        self.assertTrue(isinstance(comment, Comment))
        self.assertEqual(comment.content, self.comment_data['content'])