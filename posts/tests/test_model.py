from .test_setup import TestSetUp
from posts.models import Post, Comment
from users.models import User
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

# models test
class PostModelTest(TestSetUp):

    def create_post(self, user):
        return Post.objects.create(
            content = self.post_data['content'],
            created_by = user, 
        )
    
    def get_post(self, id):
        try:
            return Post.objects.get(id=id)
        except ObjectDoesNotExist:
            return None
    
    def delete_post(self, post):
        return post.delete()

    def test_post_creation(self):
        user = User.objects.get(email = self.user_data['email'])
        post = self.create_post(user)
        self.assertTrue(isinstance(post, Post))
        self.assertEqual(post.content, self.post_data['content'])
        self.assertEqual(post.created_by.id, user.id)

        post_retrieved = self.get_post(post.id)
        self.assertTrue(isinstance(post_retrieved, Post))
        self.assertEqual(post_retrieved.content, self.post_data['content'])
        self.assertEqual(post.created_by.id, user.id)

        post_deleted = self.delete_post(post_retrieved)
        self.assertIsNone(self.get_post(post_retrieved.id))
    
class CommentModelTest(TestSetUp):

    def create_comment(self, user):
        return Comment.objects.create(
            content = self.comment_data['content'],
            created_by = user,
        )
    
    def get_comment(self, id):
        try:
            return Comment.objects.get(id=id)
        except ObjectDoesNotExist:
            return None
    
    def delete_comment(self, comment):
        return comment.delete()

    def test_comment_creation(self):
        user = User.objects.get(email = self.user_data['email'])
        comment = self.create_comment(user)
        self.assertTrue(isinstance(comment, Comment))
        self.assertEqual(comment.content, self.comment_data['content'])
        self.assertEqual(comment.created_by.id, user.id)

        comment_retrieved = self.get_comment(comment.id)
        self.assertTrue(isinstance(comment_retrieved, Comment))
        self.assertEqual(comment_retrieved.content, self.comment_data['content'])
        self.assertEqual(comment.created_by.id, user.id)

        comment_deleted = self.delete_comment(comment_retrieved)
        self.assertIsNone(self.get_comment(comment_retrieved.id))