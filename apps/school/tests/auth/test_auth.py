from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class AuthenticationUserTestCase(APITestCase):

    def setUp(self):
        self.demo_username = 'demouser'
        self.demo_password = 'demo1234'
        self.user = User.objects.create_user(
            username=self.demo_username,
            password=self.demo_password
        )

    def test_successful_user_authentication(self):
        """ Test to verify user authentication """
        # When valid credentials are used
        user = authenticate(
            username=self.demo_username,    
            password=self.demo_password
        )

        # Then the user should be authenticated
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_unsuccessful_user_authentication(self):
        """ Test to verify if invalid data will not authenticate """
        auth_data = [
            # username      | password
            [self.demo_username, 'invalidPassword'],
            ['invalidUsername', self.demo_username],
            ['invalidUsername', 'invalidPassword']
        ]

        for username, password in auth_data:
            with self.subTest(msg=f'Logging using username={username} and password={password}'):
                # When invalid credentials are used
                user = authenticate(
                    username=username,
                    password=password
                )

                self.assertIsNone(user)
