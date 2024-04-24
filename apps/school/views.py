from rest_framework import viewsets, generics
from apps.school.models import Student, Course, Enrollment
from apps.school.serializer import StudentSerializer, CourseSerializer, \
    EnrollmentSerializer, StudentEnrollmentsSerializer, CourseEnrollmentsSerializer

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

class ListStudentEnrollments(generics.ListAPIView):
    """
    Listing all enrollments of a student
    """
    # The use of generics.ListAPIView is to create a read only endpoint

    def get_queryset(self):
        studentId = self.kwargs['pk']
        # The parameter name is defined in the urls.py as <int:pk>

        queryset = Enrollment.objects.filter(student_id=studentId)
        return queryset
    serializer_class = StudentEnrollmentsSerializer

class ListCourseEnrollments(generics.ListAPIView):
    """
    Listing all enrollments of a course
    """

    def get_queryset(self):
        courseId = self.kwargs['pk']
        queryset = Enrollment.objects.filter(course_id=courseId)
        return queryset
    serializer_class = CourseEnrollmentsSerializer
