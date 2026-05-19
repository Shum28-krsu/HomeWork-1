from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('<int:id>/', views.BookDetailView.as_view(), name='book_detail'),
]