import random

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import AddTeacherForm, AddStudentForm
from users.models import Teacher, Student


# Create your views here.
def admin_dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'admin.html')
    else:
        return redirect('admin-login')


def admin_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('admin-dashboard')
    return render(request, 'admin_login.html')


def add_teacher_view(request):
    if request.method == 'POST':
        form = AddTeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin-dashboard')
    else:
        form = AddTeacherForm()
    return render(request, 'add_teacher.html', {'form': form})


def add_student_view(request):
    if request.method == 'POST':
        form = AddStudentForm(request.POST, request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            avatar = form.cleaned_data['avatar']
            group = form.cleaned_data['group']
            phone = form.cleaned_data['phone']
            username = str(random.randint(100000, 999999))
            password = str(random.randint(10000, 99999))
            with open('student_passwords.txt', 'a') as file:
                file.write(f'{first_name} {last_name} {group.name} username:{username}, password:{password}\n')
            user  = Student.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, group=group, phone=phone, avatar=avatar)
            user.set_password(password)
            user.save()
            return redirect('admin-dashboard')
    else:
        form = AddStudentForm()
    return render(request, 'add_teacher.html', {'form': form})

def students_view(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'students.html', context)


def teachers_view(request):
    teachers = Teacher.objects.all()
    context = {'teachers': teachers}
    return render(request, 'teachers.html', context)