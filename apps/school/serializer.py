from dataclasses import field
from rest_framework import serializers
from apps.school.models import Student, Course

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
