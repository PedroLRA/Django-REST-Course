from django.contrib import admin
from apps.school.models import Student, Course

class Students(admin.ModelAdmin):
    list_display = ('id', 'name', 'doc_rg', 'doc_cpf', 'birth')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(Student, Students)

class Courses(admin.ModelAdmin):
    list_display = ('id', 'code', 'description', 'level')
    list_display_links = ('id', 'code')
    search_fields = ('id', 'code')
    list_per_page = 20

admin.site.register(Course, Courses)
