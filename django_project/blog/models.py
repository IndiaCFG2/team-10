from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Course(models.Model):
    # NICK NAME should be unique
    course_id = models.CharField(max_length=100, unique =  True)
    course_name= models.CharField(max_length=100)
    course_des = models.TextField(max_length=300)
    corse_link = models.CharField(max_length=100)
    

    def __str__(self):
        return self.course_id



# Create your models here.

class Teacher(models.Model):
    # NICK NAME should be unique
    username = models.CharField(max_length=100, unique =  True)
    teacher_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    subject = models.CharField(max_length=150)
    grade = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Student(models.Model):
    # NICK NAME should be unique
    stud_name = models.CharField(max_length=100)
    testtype = models.CharField(max_length=100)
    date_of_test = models.DateField()
    marks = models.IntegerField()

    def __str__(self):
        return self.stud_name

# class School(models.Model):
#     # NICK NAME should be unique
#     school_id = models.IntegerField(max_length=100, unique =  True)
#     name = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#     location = models.CharField(max_length=100)
#     phone = models.IntegerField()
#     principal_name = models.CharField(max_length=100)
#     teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.school_id

# class ProgramManager(models.Model):
#     # NICK NAME should be unique
#     pm_id = models.IntegerField(unique =  True)
#     name = models.CharField(max_length=100)
#     locality = models.CharField(max_length=100)
#     locality_id = models.IntegerField()
#     school = models.ForeignKey(School, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.pm_id






