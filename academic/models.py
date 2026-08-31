from django.db import models

# Create your models here.
class Teacher(models.Model):
    """Modelo para representar a los docentes de la institución."""
    first_name = models.CharField(max_length=100, verbose_name="Nombre")
    last_name = models.CharField(max_length=100, verbose_name="Apellido")

    class Meta:
        verbose_name = "Docente"
        verbose_name_plural = "Docentes"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Course(models.Model):
    """Modelo para representar las asignaturas impartidas."""
    name = models.CharField(max_length=150, verbose_name="Nombre de Asignatura")
    teacher = models.ForeignKey(
        Teacher, 
        on_delete=models.CASCADE, 
        related_name="courses", 
        verbose_name="Docente Asignado"
    )

    class Meta:
        verbose_name = "Asignatura"
        verbose_name_plural = "Asignaturas"

    def __str__(self):
        return self.name


class Student(models.Model):
    """Modelo para representar a los estudiantes registrados."""
    first_name = models.CharField(max_length=100, verbose_name="Nombre")
    last_name = models.CharField(max_length=100, verbose_name="Apellido")

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class StudentCourse(models.Model):
    """Tabla intermedia para gestionar la inscripción de alumnos en asignaturas."""
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="enrollments")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="enrollments")

    class Meta:
        verbose_name = "Inscripción de Curso"
        verbose_name_plural = "Inscripciones de Cursos"
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student} inscrito en {self.course}"