from django.test import TestCase
from rest_framework.exceptions import ValidationError
from apps.school.models import Course
from apps.school.serializers import CourseSerializer
from apps.school.error_messages import ErrorMessages

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

    def test_instanciate_serializer_with_invalid_data(self):
        """ Test to check if the serializer validators will raise an error if the data is invalid """
        invalid_list = [
            # Field         | value     | error message
            ['code',        None,       'This field may not be null.'],
            ['code',        '',         'This field may not be blank.'],
            ['code',        '1TC3',     ErrorMessages.INVALID_COURSE_CODE_FORMAT],
            ['code',        'TTT',      ErrorMessages.INVALID_COURSE_CODE_FORMAT],
            ['code',        '111',      ErrorMessages.INVALID_COURSE_CODE_FORMAT],
            ['code',        'TTTCCC2',  ErrorMessages.INVALID_COURSE_CODE_FORMAT],
            ['description', None,       'This field may not be null.'],
            ['description', '',         'This field may not be blank.'],
            ['level',       None,       'This field may not be null.'],
            ['level',       '',         '"" is not a valid choice.'],
            ['level',       'C',        '"C" is not a valid choice.'],
        ]
        # The django built-in error messages are hardcoded
        # Once new messages are added to override the default ones, this test
        # will need to be updated

        for field, value, error_msg in invalid_list:
            with self.subTest(msg=f'Trying to instanciate the serializer with invalid data: {field} = {value}'):
                # Given the invalid data
                data = {
                    'code': 'TC1',
                    'description': 'Test Course 1',
                    'level': 'A'
                }
                data.update({field: value})

                # When we try to instanciate the serializer with invalid data
                serializer = CourseSerializer(data=data)

                # Then the serializer should
                with self.assertRaises(ValidationError) as error:
                    serializer.is_valid(raise_exception=True)

                self.assertEqual(str(error.exception.detail[field][0]), error_msg)