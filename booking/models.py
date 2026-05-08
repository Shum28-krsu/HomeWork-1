from django.db import models
from travel_company.models import TourCompany


class Booking(models.Model):
    full_name = models.CharField(max_length=100)

    phone_number = models.CharField(max_length=100)

    choice_company = models.ForeignKey(
        TourCompany,
        on_delete=models.CASCADE,
        related_name='bookings'
    )

    date_tour = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} --- {self.choice_company}"