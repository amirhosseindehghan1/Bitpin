from django.test import TestCase, Client
from .models import BlogPost, Rating
from django.contrib.auth.models import User
from .serializers import BlogPostSerializer, RatingSerializer
from rest_framework import status
import json

class BlogPostModelTest(TestCase):

    def test_average_rating(self):
        user1 = User.objects.create(username='user1')
        user2 = User.objects.create(username='user2')
        blog_post = BlogPost.objects.create(title='Test Post', description='This is a test post')

        Rating.objects.create(points=4, user=user1, blog_post=blog_post)
        Rating.objects.create(points=2, user=user2, blog_post=blog_post)

        self.assertEqual(blog_post.average_rating(), 3.0)

class BlogPostSerializerTest(TestCase):

    def test_serialization(self):
        user = User.objects.create(username='user1')
        blog_post = BlogPost.objects.create(title='Test Post', description='This is a test post')
        Rating.objects.create(points=4, user=user, blog_post=blog_post)

        serializer = BlogPostSerializer(blog_post)
        expected_data = {
            'id': blog_post.id,
            'title': 'Test Post',
            'description': 'This is a test post',
            'num_ratings': 1,
            'average_rating': 4.0,
        }
        self.assertEqual(serializer.data, expected_data)

class BlogPostViewSetTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_list_blog_posts(self):
        response = self.client.get('/api/blogposts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_blog_post(self):
        self.client.login(username='testuser', password='testpassword')
        data = {
            'title': 'Test Post',
            'description': 'This is a test post',
        }
        response = self.client.post('/api/blogposts/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

