from django.test import Client, TestCase
from posts.models import Post, User
from django.contrib.auth import get_user_model
from posts.models import Post, User, Follow


User = get_user_model()


class FollowTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='Ss')
        cls.post = Post.objects.create(
            author=cls.user,
            text='Тестовая пост for follow',
        )
        cls.author = cls.user

    def setUp(self):
        self.user_1 = User.objects.create_user(username='follower')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user_1)

    def test_folow(self):
        followers = Follow.objects.all()
        follower = Follow.objects.create(
            user=self.user, author=self.author)
        self.assertTrue(follower, followers)
        self.check_url(self.user_1, f'/profile/{self.user.username}/follow', '/profile/<username>/follow/')
        assert Follow.objects.follower.count() == 1