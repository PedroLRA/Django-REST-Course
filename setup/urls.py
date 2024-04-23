from django.contrib import admin
from django.urls import path
from apps.school.views import student

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', student, name='student'),
]
