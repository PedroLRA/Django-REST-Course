from rest_framework import serializers
from apps.school.models import Student, Course, Enrollment
from apps.school.validators import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        exclude = ['phone_number'] 
        # If we don't want all the fields, we can give a list with the desired
        # ones: fields = ['id', 'name']
        # This way the serializer can be used as a filter between the DB
        # and the API

    # Validations
    def validate(self, data):
        run_validators(
            data,
            validators = {
                'name': validate_name,
                'doc_rg': validate_doc_rg,
                'doc_cpf': validate_doc_cpf,
                'birth': validate_birth
            }
        )

        return data

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

    # Validations
    def validate(self, data):
        # Since in this case we only have one field to use a custom validation,
        # we can skip the use of the run_validators function.
        # But, we will still use it in case of future need of more validations.
        run_validators(data, validators = {'code': validate_code})
        return data

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        exclude = []
        # Using the exclude attribute we can remove the given fields from the 
        # serialization.
        # We also can pass the attribute without any fields inside the list to
        # represent all the fields:
        #   exclude = [] is basically the same as fields = '__all__'

class StudentEnrollmentsSerializer(serializers.ModelSerializer):
    # Changing the values that will be displayed for course and shift in the API:
    course = serializers.ReadOnlyField(source='course.description')

    # To change the shift display , we can also user the ReadOnlyField and pass
    # the source as the get method of the model:
    #   shift = serializers.ReadOnlyField(source='get_shift_display')
    # or we can use the following:
    shift = serializers.SerializerMethodField()
    def get_shift(self, obj):
        return obj.get_shift_display()

    class Meta:
        model = Enrollment
        fields = ['course', 'shift']

class CourseEnrollmentsSerializer(serializers.ModelSerializer):
    # Changing the values displayed for student and shift in the API:
    student_name = serializers.ReadOnlyField(source='student.name')
    shift = serializers.ReadOnlyField(source='get_shift_display')

    class Meta:
        model = Enrollment
        fields = ['student_name', 'shift']

## Serializers Version 2
class StudentSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__' 
        # If we don't want all the fields, we can give a list with the desired
        # ones: fields = ['id', 'name']
        # This way the serializer can be used as a filter between the DB
        # and the API

    # Validations
    def validate(self, data):
        run_validators(
            data,
            validators = {
                'name': validate_name,
                'doc_rg': validate_doc_rg,
                'doc_cpf': validate_doc_cpf,
                'birth': validate_birth
            }
        )
        return data
