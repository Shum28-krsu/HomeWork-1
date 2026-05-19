from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from . import models
from .forms import BookingForm


class BookingListView(ListView):
    model = models.Booking
    template_name = 'booking/booking_list.html'
    context_object_name = 'bookings'


class BookingCreateView(CreateView):
    model = models.Booking
    form_class = BookingForm
    template_name = 'booking/booking_form.html'
    success_url = reverse_lazy('booking_list')


class BookingUpdateView(UpdateView):
    model = models.Booking
    form_class = BookingForm
    template_name = 'booking/booking_form.html'
    success_url = reverse_lazy('booking_list')
    pk_url_kwarg = 'id'


class BookingDeleteView(DeleteView):
    model = models.Booking
    template_name = 'booking/booking_delete.html'
    success_url = reverse_lazy('booking_list')
    context_object_name = 'booking'
    pk_url_kwarg = 'id'