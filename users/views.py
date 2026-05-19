from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, LoginForm
from .models import CustomUser


def register_view(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('ankets')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {
        'form': form
    })

def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(
                request,
                username=username,
                password=password
            )
            if user is not None:
                login(request, user)
                return redirect('ankets')
    return render(request, 'users/login.html', {
        'form': form
    })

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def ankets_view(request):
    users = CustomUser.objects.all()
    return render(request, 'users/ankets.html', {
        'users': users
    })