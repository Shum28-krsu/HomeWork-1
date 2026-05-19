from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from captcha.fields import CaptchaField

from .models import CustomUser


class RegisterForm(UserCreationForm):

    class Meta:

        model = CustomUser

        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'phone',
            'birth_date',
            'city',
            'education',
            'experience',
            'skills',
            'resume_file',
            'photo',
            'password1',
            'password2',
        ]


class LoginForm(AuthenticationForm):

    captcha = CaptchaField()