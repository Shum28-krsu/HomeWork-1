from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from .forms import BookingForm

def booking_list(request):
    bookings = Booking.objects.all()

    return render(request, 'booking/booking_list.html', {
        'bookings': bookings
    })

def booking_create(request):
    form = BookingForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('booking_list')

    return render(request, 'booking/booking_form.html', {
        'form': form
    })

def booking_update(request, id):
    booking = get_object_or_404(Booking, id=id)

    form = BookingForm(request.POST or None, instance=booking)

    if form.is_valid():
        form.save()
        return redirect('booking_list')

    return render(request, 'booking/booking_form.html', {
        'form': form
    })


def booking_delete(request, id):
    booking = get_object_or_404(Booking, id=id)

    if request.method == 'POST':
        booking.delete()
        return redirect('booking_list')

    return render(request, 'booking/booking_delete.html', {
        'booking': booking
    })