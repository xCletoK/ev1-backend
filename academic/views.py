# academic/views.py
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Teacher, Course, Student
from .serializers import TeacherSerializer, CourseSerializer, StudentSerializer

# 1. VISTAS HTML (FRONTEND SHELL)
def home_view(request):
    """Renderiza la vista principal o redirige a cursos."""
    return render(request, 'academic/courses.html')

def courses_view(request):
    """Renderiza el cascarón HTML para el listado de cursos."""
    return render(request, 'academic/courses.html')

def students_view(request):
    """Renderiza el cascarón HTML para el listado de estudiantes."""
    return render(request, 'academic/students.html')


# 2. ENDPOINTS REST API (DRF)
@api_view(['GET'])
def api_courses(request):
    """Endpoint que retorna el listado de asignaturas en formato JSON."""
    courses = Course.objects.select_related('teacher').all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def api_students(request):
    """Endpoint que retorna el listado de estudiantes en formato JSON."""
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def api_teachers(request):
    """Endpoint que retorna el listado de docentes en formato JSON."""
    teachers = Teacher.objects.all()
    serializer = TeacherSerializer(teachers, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)