from django.urls import path
from . import views


urlpatterns = [
    path('', views.booking_list, name='booking_list'),

    path('create/', views.booking_create, name='booking_create'),

    path('update/<int:id>/', views.booking_update, name='booking_update'),

    path('delete/<int:id>/', views.booking_delete, name='booking_delete'),
]