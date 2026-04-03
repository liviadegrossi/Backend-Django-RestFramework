from school.models import Student, Course, Enrollment
from school.serializers import StudentSerializer, CourseSerializer, EnrollmentSerializer, ListEnrollmentStudentSerializer, ListEnrollmentCourseSerializer
from rest_framework import viewsets, generics
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # defined in the settings
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # defined in the settings
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    # defined in the settings
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

class EnrollmentStudent(generics.ListAPIView):
    def get_queryset(self):
        queryset = Enrollment.objects.filter(student_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListEnrollmentStudentSerializer
    # defined in the settings
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

class EnrollmentCourse(generics.ListAPIView):
    def get_queryset(self):
        queryset = Enrollment.objects.filter(course_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListEnrollmentCourseSerializer
    # defined in the settings
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
