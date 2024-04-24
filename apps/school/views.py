from rest_framework import viewsets
from apps.school.models import Student, Course, Enrollment
from apps.school.serializer import StudentSerializer, CourseSerializer, \
    EnrollmentSerializer

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

class EnrollmentsViewSet(viewsets.ModelViewSet):
    """
    Display all Enrollments in the DB
    """

    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
