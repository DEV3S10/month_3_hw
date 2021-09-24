from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=150)
    major = models.CharField(max_length=100)
    direction = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=1)


class Blog(models.Model):
    image = models.ImageField(upload_to="blog_pics/")
    title = models.CharField(max_length=150)
    description = models.TextField()
    hashtags = models.TextField()


class Comment(models.Model):
    class Meta:
        ordering = ['-datetime']
    text = models.TextField()
    datetime = models.DateTimeField(auto_now=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
