from django.db import models
from django.contrib.auth.models import User

class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=25, default="Add your name")
    surname = models.CharField(max_length=25, default="Add your surname")
    age = models.IntegerField(default=18)
    email = models.EmailField(default="Add your email")
    phone_number = models.CharField(max_length=20, default="Add your phone number")
    experience = models.TextField(default="Add your experience")
    education = models.TextField(default="Add your education")
    skills = models.TextField(default="Add your skills")
    salary = models.CharField(max_length=20, default="Add your salary expectation")


    resume_file = models.FileField(upload_to='resumes/',  blank=True)
    photo = models.ImageField(upload_to='photos/', blank=True)

    def __str__(self):
        return f"{self.name} {self.surname}"
