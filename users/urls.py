from django.urls import include, path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('resumes/', views.resume_list, name='resume_list'),

    path('captcha/', include('captcha.urls')),
]