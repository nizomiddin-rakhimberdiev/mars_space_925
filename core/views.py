import random

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import AddTeacherForm, AddStudentForm, AddGroupForm, EditStudentForm
from users.models import Teacher, Student, Group


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
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            password = f"{random.randint(10000, 99999)}{first_name}"
            with open('teachers.txt', 'a') as f:
                f.write(f"FirstName: {first_name}, Last Name: {last_name}, Username: {username}, Password: {password}\n")
            Teacher.objects.create(first_name=first_name, last_name=last_name,username=username, password=password)
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
    search_query = request.GET.get('search', '')
    if search_query:
        students = Student.objects.filter(first_name__icontains=search_query)
    else:
        students = Student.objects.all()
    context = {'students': students}
    return render(request, 'students.html', context)


def teachers_view(request):
    teachers = Teacher.objects.all()
    context = {'teachers': teachers}
    return render(request, 'teachers.html', context)


def add_group_view(request):
    if request.method == 'POST':
        form = AddGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin-dashboard')
    elif request.method == 'GET':
        form = AddGroupForm()
    return render(request, 'add_teacher.html', {'form': form})


def groups_view(request):
    groups = Group.objects.all()
    context = {'groups': groups}
    return render(request, 'groups.html', context)


def edit_student_view(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        form = EditStudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = EditStudentForm(instance=student)
    return render(request, 'add_teacher.html', {'form': form})