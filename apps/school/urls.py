from rest_framework import routers
from django.urls import path
from apps.school.views import StudentsViewSet, CoursesViewSet, \
    EnrollmentsViewSet, ListStudentEnrollments, ListCourseEnrollments

school_router = routers.DefaultRouter()
school_router.register('students', StudentsViewSet, basename='Students')
school_router.register('courses', CoursesViewSet, basename='Courses')
school_router.register('enrollments', EnrollmentsViewSet, basename='Enrollments')

# Defining more specific routes that uses parameters
urlpatterns = [
    path(
        'student/<int:pk>/enrollments/',
        ListStudentEnrollments.as_view(),
        name='StudentEnrollments'
    ),
    path(
        'course/<int:pk>/enrollments/',
        ListCourseEnrollments.as_view(),
        name='CourseEnrollments'
    ),
]
