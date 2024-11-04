from django.urls import path

from .views import admin_dashboard, admin_login_view, add_teacher_view, teachers_view, add_student_view, students_view

urlpatterns = [
    path('admin-login/', admin_login_view, name='admin-login'),
    path('', admin_dashboard, name='admin-dashboard'),
    path('add-teacher/', add_teacher_view, name='add-teacher'),
    path('add-student/', add_student_view, name='add-student'),
    path('teachers/', teachers_view, name='teachers'),
    path('students/', students_view, name='students'),
]