from django.contrib.admindocs.utils import ROLES
from django.contrib.auth.models import AbstractUser
from django.db import models
import random


class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # related_name bilan to'qnashuv oldini olish
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set_permissions',  # related_name bilan to'qnashuv oldini olish
        blank=True
    )

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        # Agar parol allaqachon hashlanmagan bo'lsa, uni hashlang
        if not self.password.startswith('pbkdf2_'):
            self.set_password(self.password)
        super().save(*args, **kwargs)


class Teacher(CustomUser):
    salary = models.DecimalField(max_digits=11, decimal_places=2, default=0)
    rating = models.IntegerField(default=0)
    rating_number = models.DecimalField(max_digits=3, decimal_places=1, default=0)


class Group(models.Model):
    DAYS = (
        ('Even', 'Even'),
        ('Odd', 'Odd'),
        ('Weekend', 'Weekend')
    )
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='group_teacher')
    day = models.CharField(max_length=10, choices=DAYS)
    start_date = models.DateField()
    end_date = models.DateField()
    lesson_time = models.TimeField()
    payment_summa = models.DecimalField(max_digits=9, decimal_places=2, default=1090000.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Create your models here.


class Student(CustomUser):
    LIGAS = (
        ('Hacker', 'Hacker'),
        ('Coder', 'Coder'),
        ('Gamer', 'Gamer'),
    )
    liga = models.CharField(max_length=10, choices=LIGAS, default=random.choice(LIGAS)[0])
    coins = models.IntegerField(default=0)
    avatar = models.ImageField(upload_to='students/avatars/')
    phone = models.CharField(max_length=13)
    xp = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='student_group')


class Admin(CustomUser):
    phone = models.CharField(max_length=13)
    salary = models.DecimalField(max_digits=11, decimal_places=2, default=0)
    kpi = models.DecimalField(max_digits=11, decimal_places=2, default=0)
