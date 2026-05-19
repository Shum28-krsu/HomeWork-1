from django.urls import path
from . import views

urlpatterns = [
    path('', views.CompanyListView.as_view(), name='company_list'),
    path('search/', views.CompanySearchView.as_view(), name='company_search'),
]