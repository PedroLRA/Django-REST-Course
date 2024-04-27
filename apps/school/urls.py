from rest_framework import routers
from django.urls import path, include
from apps.school.views import StudentsViewSet, CoursesViewSet, \
    EnrollmentsViewSet, ListStudentEnrollments, ListCourseEnrollments

school_router = routers.DefaultRouter()
school_router.register('students', StudentsViewSet, basename='Students')
school_router.register('courses', CoursesViewSet, basename='Courses')
school_router.register('enrollments', EnrollmentsViewSet, basename='Enrollments')

# Defining more specific routes that uses parameters
urlpatterns = [
    # Include the default routes defined in the router
    path('', include(school_router.urls)),
    path(
        'students/<int:pk>/enrollments/',
        ListStudentEnrollments.as_view(),
        name='StudentEnrollments'
    ),
    path(
        'courses/<int:pk>/enrollments/',
        ListCourseEnrollments.as_view(),
        name='CourseEnrollments'
    ),
]
