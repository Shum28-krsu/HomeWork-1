from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, RedirectView

from .forms import RegisterForm, LoginForm
from . import models


class RegisterView(CreateView):
    model = models.CustomUser
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('ankets')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    authentication_form = LoginForm

    def get_success_url(self):
        return reverse_lazy('ankets')


class LogoutView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        return reverse_lazy('login')


class AnketsView(LoginRequiredMixin, ListView):
    model = models.CustomUser
    template_name = 'users/ankets.html'
    context_object_name = 'users'

    def get_queryset(self):
        return models.CustomUser.objects.all()