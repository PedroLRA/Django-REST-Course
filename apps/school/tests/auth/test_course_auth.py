from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.urls import reverse

class CourseUserAuthenticationTestCase(APITestCase):

    def setUp(self):
        self.demo_username = 'demouser'
        self.demo_password = 'demo1234'
        self.user = User.objects.create_user(
            username=self.demo_username,
            password=self.demo_password
        )

        self.list_url = reverse('Courses-list')

        self.client = APIClient()

    def tearDown(self):
        self.client.force_authenticate(None) #removing authentication
        self.client.logout() 

    def test_authenticated_request_to_courses_endpoint(self):
        """ Test to verify authenticated request to courses endpoint """
        # Given an authenticated session
        login = self.client.login(
            username=self.demo_username,
            password=self.demo_password
        )
        self.assertTrue(login, msg='Invalid login') # Check if the loggin is possible
        self.client.force_authenticate(self.user) # set authentication

        # When a request is made
        response = self.client.get(self.list_url)

        # Then the response should
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_request_to_courses_endpoint(self):
        """ Test to verify unauthenticated request to courses endpoint """
        # When an unauthenticated request is made
        response = self.client.get(self.list_url)

        # Then the response should
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
