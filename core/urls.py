from django.urls import path

from .views import admin_dashboard, admin_login_view, add_teacher_view, teachers_view, add_student_view, students_view, \
    add_group_view, groups_view, edit_student_view

urlpatterns = [
    path('admin-login/', admin_login_view, name='admin-login'),
    path('', admin_dashboard, name='admin-dashboard'),
    path('add-teacher/', add_teacher_view, name='add-teacher'),
    path('add-student/', add_student_view, name='add-student'),
    path('add-group/', add_group_view, name='add-group'),
    path('teachers/', teachers_view, name='teachers'),
    path('students/', students_view, name='students'),
    path('groups/', groups_view, name='groups'),
    path('edit-student/<int:id>/', edit_student_view, name='edit-student')
]