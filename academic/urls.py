from django.urls import path
from . import views

urlpatterns = [
    # Vistas Web (Frontend enmascarado)
    path('', views.courses_view, name='home'),
    path('courses/', views.courses_view, name='courses_view'),
    path('students/', views.students_view, name='students_view'),

    # Endpoints API REST
    path('api/courses/', views.api_courses, name='api_courses'),
    path('api/students/', views.api_students, name='api_students'),
    path('api/teachers/', views.api_teachers, name='api_teachers'),
]