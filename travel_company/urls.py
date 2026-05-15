from django.urls import path
from . import views

urlpatterns = [
    path('travel_company/', views.company_list, name='company_list'),
    path('travel_company/search/', views.search_view_c, name='company_search'),
]