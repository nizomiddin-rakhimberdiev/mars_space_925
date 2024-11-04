from django.urls import path

from teachers.views import teacher_dashboard, teacher_login_view, detail_group, logout_view

urlpatterns = [
    path('', teacher_dashboard, name='teacher_dashboard'),
    path('teacher-login/', teacher_login_view, name='teacher-login'),
    path('group_detail/<int:id>/', detail_group, name='group-detail'),
    path('logout/', logout_view, name='logout')
]