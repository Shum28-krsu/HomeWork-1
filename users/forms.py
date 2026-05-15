from django import forms
from captcha.fields import CaptchaField
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from . import models


class ResumeForm(forms.ModelForm):
    class Meta:
        model = models.Resume
        fields = [
            'name',
            'surname',
            'age',
            'email', 
            'phone_number', 
            'experience', 
            'education',
            'skills', 
            'salary', 
            'resume_file', 
            'photo'
            ]
        
class Meta:
    model = User
    fields = '__all__'




class MyForm(forms.Form):
    CAPTCHA_LENGTH = 5  
    CAPTCHA_IMAGE_SIZE = (150, 50)  

    captcha = CaptchaField()
