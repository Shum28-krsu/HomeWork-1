from django.urls import path
from . import views

urlpatterns = [
    path('quote_a/', views.quote_a, name = 'quote_a'),
    path('quote_b/', views.quote_b, name = 'quote_b'),
    path('quote_c/', views.quote_c, name = 'quote_c'),

    #HOMEWORK 2
    path('book_list/', views.book_list, name='book_list'),
    path('book_detail/<int:id>/', views.book_detail, name='book_detail'),
]