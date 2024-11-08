from django import forms
from users.models import Teacher, Student, Group


class AddTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'username']


class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'avatar', 'group', 'phone']


class EditStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'avatar', 'group', 'phone']


class AddGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'course', 'teacher', 'day', 'start_date', 'end_date', 'lesson_time']