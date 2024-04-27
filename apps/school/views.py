from rest_framework import viewsets, generics, filters
from apps.school.models import Student, Course, Enrollment
from django_filters.rest_framework import DjangoFilterBackend
from apps.school.serializer import StudentSerializer, StudentSerializerV2, \
    CourseSerializer, EnrollmentSerializer, StudentEnrollmentsSerializer, \
    CourseEnrollmentsSerializer

class StudentsViewSet(viewsets.ModelViewSet):
    """
    Display all students in the DB
    """

    queryset = Student.objects.all()

    #Applying filters and ordering
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    ]
    ordering_fields = ['name']
    search_fields = ['name', 'doc_rg', 'doc_cpf']

    def get_serializer_class(self):
        if self.request.version == '2':
            return StudentSerializerV2
        
        return StudentSerializer

class CoursesViewSet(viewsets.ModelViewSet):
    """
    Display all Courses in the DB
    """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    #Applying filters and ordering
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    ]
    ordering_fields = ['code']
    search_fields = ['code']
    filterset_fields = ['level']

class EnrollmentsViewSet(viewsets.ModelViewSet):
    """
    Display all Enrollments in the DB
    """

    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

    #Applying filters and ordering
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    ]
    ordering_fields = ['student', 'course']
    search_fields = ['student', 'course']
    filterset_fields = ['shift']

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

    #Applying filters and ordering
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    ]
    ordering_fields = ['course']
    search_fields = ['course']
    filterset_fields = ['shift']

class ListCourseEnrollments(generics.ListAPIView):
    """
    Listing all enrollments of a course
    """

    def get_queryset(self):
        courseId = self.kwargs['pk']
        queryset = Enrollment.objects.filter(course_id=courseId)
        return queryset
    serializer_class = CourseEnrollmentsSerializer

    #Applying filters and ordering
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    ]
    ordering_fields = ['student']
    search_fields = ['student']
    filterset_fields = ['shift']