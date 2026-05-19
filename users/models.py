from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    phone = models.CharField(max_length=20)
    birth_date = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=100)
    education = models.TextField()
    experience = models.TextField()
    skills = models.TextField()
    resume_file = models.FileField(upload_to='resumes/')
    photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.username