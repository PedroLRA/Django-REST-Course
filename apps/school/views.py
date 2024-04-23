from rest_framework import viewsets
from apps.school.models import Student, Course
from apps.school.serializer import StudentSerializer, CourseSerializer

class StudentsViewSet(viewsets.ModelViewSet):
    """
    Display all students in the DB
    """

    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CoursesViewSet(viewsets.ModelViewSet):
    """
    Display all Courses in the DB
    """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
