from django.contrib import admin
from apps.school.models import Student, Course, Enrollment

class Students(admin.ModelAdmin):
    list_display = ('id', 'name', 'doc_rg', 'doc_cpf', 'birth')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'doc_rg', 'doc_cpf')
    list_per_page = 20
    ordering = ('name',)

admin.site.register(Student, Students)

class Courses(admin.ModelAdmin):
    list_display = ('id', 'code', 'description', 'level')
    list_display_links = ('id', 'code')
    search_fields = ('id', 'code')
    list_filter = ('level',)
    list_per_page = 20
    ordering = ('code',)

admin.site.register(Course, Courses)

class Enrollments(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'shift')
    list_display_links = ('id',)
    search_fields = ('id', 'course', 'student')
    list_filter = ('shift',)
    list_per_page = 20
    ordering = ('student', 'course')

admin.site.register(Enrollment, Enrollments)
