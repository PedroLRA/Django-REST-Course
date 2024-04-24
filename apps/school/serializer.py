from rest_framework import serializers
from apps.school.models import Student, Course, Enrollment

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__' 
        # If we don't want all the fields, we can give a list with the desired
        # ones: fields = ['id', 'name']
        # This way the serializer can be used as a filter between the DB
        # and the API

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

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
        