from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from users.models import Group, Teacher, Student


# Create your views here.
def teacher_dashboard(request):
    if request.user.is_authenticated:
        groups = Group.objects.filter(teacher=request.user)
        teacher = Teacher.objects.get(username=request.user.username)
        context = {
            'groups': groups,
            'teacher': teacher,
        }
        return render(request, 'teacher_dashboard.html', context)
    else:
        return redirect('teacher-login')


def teacher_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('teacher_dashboard')
    return render(request, 'admin_login.html')


def detail_group(request, id):
    group = Group.objects.get(pk=id)
    students = Student.objects.filter(group=group)
    context = {
        'group': group,
        'students': students,
    }
    return render(request, 'group_detail.html', context)


def logout_view(request):
    logout(request)
    return redirect('teacher-login')