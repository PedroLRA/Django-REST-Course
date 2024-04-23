from rest_framework import routers
from apps.school.views import StudentsViewSet, CoursesViewSet

school_router = routers.DefaultRouter()
school_router.register('students', StudentsViewSet, basename='Students')
school_router.register('courses', CoursesViewSet, basename='Courses')