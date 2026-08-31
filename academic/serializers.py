from rest_framework import serializers
from .models import Teacher, Course, Student, StudentCourse

class TeacherSerializer(serializers.ModelSerializer):
    """Serializador para la entidad Docente."""
    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name']


class CourseSerializer(serializers.ModelSerializer):
    """Serializador para la entidad Asignatura, incluyendo datos legibles del docente."""
    teacher_name = serializers.ReadOnlyField(source='teacher.__str__')

    class Meta:
        model = Course
        fields = ['id', 'name', 'teacher', 'teacher_name']


class StudentSerializer(serializers.ModelSerializer):
    """Serializador para la entidad Estudiante."""
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name']


class StudentCourseSerializer(serializers.ModelSerializer):
    """Serializador para inscripciones de asignaturas."""
    student_name = serializers.ReadOnlyField(source='student.__str__')
    course_name = serializers.ReadOnlyField(source='course.name')

    class Meta:
        model = StudentCourse
        fields = ['id', 'student', 'student_name', 'course', 'course_name']