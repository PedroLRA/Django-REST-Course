from django.contrib import admin
from django.urls import path, include
from apps.school.urls import school_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(school_router.urls)),
]
