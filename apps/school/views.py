from rest_framework import viewsets, generics, filters
from apps.school.models import Student, Course, Enrollment
from django_filters.rest_framework import DjangoFilterBackend
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from apps.school.serializer import StudentSerializer, StudentSerializerV2, \
    CourseSerializer, EnrollmentSerializer, StudentEnrollmentsSerializer, \
    CourseEnrollmentsSerializer
from apps.school.utils.viewsUtils import response_with_location

class StudentsViewSet(viewsets.ModelViewSet):
    """
    Display all students in the DB
    """

    # To define specif http methods, we can use the following:
    # http_method_names = ['get', 'post', 'put', 'patch']

    queryset = Student.objects.all()

    #Applying filters and ordering
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    ]
    ordering_fields = ['name']
    search_fields = ['name', 'doc_rg', 'doc_cpf']

    # Defining the serializer class based on the version of the API
    # This consists in a overriden method to return the correct serializer
    def get_serializer_class(self):
        if self.request.GET.get('version') == '2':
            return StudentSerializerV2
        return StudentSerializer

    # Overriding the create method to add a custom response
    def create(self, request):
        return response_with_location(self, request)

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

    # Overriding the create method to add a custom response
    def create(self, request):
        return response_with_location(self, request)

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

    # Overriding the create method to add a custom response
    def create(self, request):
        return response_with_location(self, request)

    # Saving the information in the cache for 60 seconds
    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

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