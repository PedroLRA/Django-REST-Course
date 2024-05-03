from django.test import TestCase
from apps.school.models import Course
from apps.school.serializers import CourseSerializer

class CourseSerializerTestCase(TestCase):

    def setUp(self):
        self.course = Course(
            code = 'TC1',
            description = 'Test Course 1',
            level = 'A'
        )

    def test_contains_expected_fields(self):
        """ Test to check the fields in the serializer """
        # When the serializer is a instance of a course
        serializer = CourseSerializer(instance=self.course)
        data = serializer.data
        expected_fields = ['id', 'code', 'description', 'level']

        # Then the serializer should contain the expected fields
        self.assertEqual(set(data.keys()), set(expected_fields))

    def test_contains_expected_content_on_each_field(self):
        """ Test to check the content of the fields in the serializer """
        # When the serializer is a instance of a course
        serializer = CourseSerializer(instance=self.course)
        data = serializer.data

        # Then the serializer should contain the expected fields
        for field_name in data.keys():
            # Since we have the field name as an string, we can use the dunder
            # method __dict__ to access the field in the course object
            # This way we can compare the serializer field with the course field
            self.assertEqual(data[field_name], self.course.__dict__[field_name])
