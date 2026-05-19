from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookingListView.as_view(), name='booking_list'),
    path('create/', views.BookingCreateView.as_view(), name='booking_create'),
    path('update/<int:id>/', views.BookingUpdateView.as_view(), name='booking_update'),
    path('delete/<int:id>/', views.BookingDeleteView.as_view(), name='booking_delete'),
]