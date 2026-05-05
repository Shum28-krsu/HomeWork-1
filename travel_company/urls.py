from django.urls import path
from . import views

urlpatterns = [
    path('travel_company/', views.company_list, name='company_list'),
]
