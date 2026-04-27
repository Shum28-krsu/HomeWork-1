from django.urls import path
from . import views

urlpatterns = [
    path('quote_a/', views.quote_a, name = 'quote_a'),
    path('quote_b/', views.quote_b, name = 'quote_b'),
    path('quote_c/', views.quote_c, name = 'quote_c'),
]