from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from school.views import StudentViewSet, CourseViewSet, EnrollmentViewSet, EnrollmentCourse, EnrollmentStudent

router = routers.DefaultRouter()
router.register('students', StudentViewSet, basename='Students')
router.register('courses', CourseViewSet, basename='Courses')
router.register('enrollments', EnrollmentViewSet, basename='Enrollments')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('students/<int:pk>/enrollments/', EnrollmentStudent.as_view()),
    path('courses/<int:pk>/courses/', EnrollmentCourse.as_view()),
]
