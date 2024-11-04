from django.db import models

from users.models import Teacher, Student


# Create your models here.



class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images/')
    price = models.IntegerField()
    count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Shop_history(models.Model):
    STATUSES = (
        ('pending', 'pending'),
        ('completed', 'completed'),
        ('cancelled', 'cancelled')
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUSES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.product.name} - {self.customer.username}'


class Blog(models.Model):
    content = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog_images/')
    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author.username} - {self.content[:50]}"

class BlogLike(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.username} - {self.blog.content[:50]}"

class Commentary(models.Model):
    content = models.CharField(max_length=255)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.username} - {self.content[:50]}"


class News(models.Model):
    banner = models.ImageField(upload_to='news_images/')
    created_at = models.DateTimeField(auto_now_add=True)


