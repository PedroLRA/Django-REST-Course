from django.core.exceptions import ValidationError
from django.test import TestCase
from apps.school.models import Course

class CourseModelTestCase(TestCase):
    def setUp(self):
        self.data = {
            'code' : 'TC1',
            'description' : 'Test Course description',
            'level' : 'A'
        }

    def test_successful_course_instantiation(self):
        """ Test to check a successful instantiation of course """
        # When a new course is instantiated
        new_course = Course(
            code=self.data['code'],
            description=self.data['description'],
            level=self.data['level']
    )

        # Then the course should have the same data
        self.assertEqual(new_course.code, self.data['code'])
        self.assertEqual(new_course.description, self.data['description'])
        self.assertEqual(new_course.level, self.data['level'])

    def test_unsuccessful_course_instantiation(self):
        """ Test to check an unsuccessful instantiation of course """
        invalid_values = [
            {'code':None},
            {'code':''},
            {'code':'TTTCCC222222444'},
            {'description':None},
            {'description':''},
            {'description':'A' * 101},
            {'level':None},
            {'level':''},
            {'level':'C'}
        ]

        for value in invalid_values:
            with self.subTest(msg=f'Trying to instantiate a course with invalid data: {value}'):
                # Given invalid data:
                invalid_data = self.data.copy()
                invalid_data.update(value)

                # When a new course is instantiated
                new_course = Course(
                    code=invalid_data['code'],
                    description=invalid_data['description'],
                    level=invalid_data['level']
                )

                # Then the course should not be saved
                with self.assertRaises(ValidationError):
                    new_course.full_clean() # check if the model is valid
                    new_course.save() # try to save the model
                self.assertEqual(Course.objects.count(), 0)
