from django.test import TestCase
from django.contrib.auth.models import User
from .models import Posts

class PostModelTests(TestCase):

    def setUp(self):
       User.objects.create(
           first_name='MyName',
           last_name="MNySurname",
           email="testuser@test.com"
       )

    def test_post_add(self):
        user = User.objects.get(pk=1)
        post = Posts(userId=user, title='Test Post', body='Sample body')
        post.save()
        self.assertEquals(Posts.objects.get(pk=1).title, 'Test Post')