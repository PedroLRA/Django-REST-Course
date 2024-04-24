from rest_framework import routers
from apps.school.views import StudentsViewSet, CoursesViewSet, EnrollmentsViewSet

school_router = routers.DefaultRouter()
school_router.register('students', StudentsViewSet, basename='Students')
school_router.register('courses', CoursesViewSet, basename='Courses')
school_router.register('enrollments', EnrollmentsViewSet, basename='Enrollments')