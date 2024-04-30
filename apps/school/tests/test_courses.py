from rest_framework.test import APITestCase, APIRequestFactory, \
    force_authenticate
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from apps.school.models import Course
from apps.school.views import CoursesViewSet

class CourseTestCase(APITestCase):

    def setUp(self):
        # Initializing the APIRequestFactory
        self.factory = APIRequestFactory()

        # Creating a demo user
        self.demoUser = User.objects.create_user(
            username='demoUser', password='password'
        )
        # giving permissions to the demo user
        content_type = ContentType.objects.get_for_model(Course)
        permissions = Permission.objects.filter(content_type=content_type)
        self.demoUser.user_permissions.set(permissions)

        # Defining the list of URLs to Courses
        self.list_url = reverse('Courses-list')

        # Creating two demo Courses 
        self.curso_1 = Course.objects.create(
            code = 'TC1',
            description = 'Test Course 1',
            level = 'A'
        )
        self.curso_2 = Course.objects.create(
            code = 'TC2',
            description = 'Test Course 2',
            level = 'B'
        )

    def test_GET_request_to_list_courses(self):
        """ Test to check GET request to list courses """
        # Given an authenticated get request
        request = self.factory.get(self.list_url)
        force_authenticate(request, user=self.demoUser)

        # When the request is made
        view = CoursesViewSet.as_view({'get': 'list'})
        response = view(request)

        # Then the response should:
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get('results')), 2)

    def test_successful_POST_request_to_create_course(self):
        """ Test to check POST request to create a new course """
        # Given a valid post request
        post_data= {
            'code': 'TC3',
            'description': 'Test Course 3',
            'level': 'A'
        }
        request = self.factory.post(self.list_url, post_data, format='json')
        force_authenticate(request, user=self.demoUser)

        # When the request is made
        view = CoursesViewSet.as_view({'post': 'create'})
        response = view(request)
        
        # Then the response should:
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        post_data.update({'id': 3}) # adding the expected id to posted data to compare
        self.assertEqual(response.data, post_data)

    def test_failure_POST_request_to_create_course(self):
        """ Test to check fail POST request when invalid data is sent"""
        test_values = [
            {'code':None},
            {'code':''},
            {'code':'1TC3'},
            {'code':'TTT'},
            {'code':'111'},
            {'code':'TTTCCC2'},
            {'description':None},
            {'description':''},
            {'level':None},
            {'level':''},
            {'level':'C'}
        ]
        
        for value in test_values:
            with self.subTest(value=value):
                # Given a post request
                post_data = {
                    'code': 'TC3',
                    'description': 'Test Course 3',
                    'level': 'A'
                }
                post_data.update(value) # updating dict with the invalid value
                request = self.factory.post(self.list_url, post_data, format='json')
                force_authenticate(request, user=self.demoUser)

                # When the request is made
                view = CoursesViewSet.as_view({'post': 'create'})
                response = view(request)
                
                # Then the response should:
                self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

