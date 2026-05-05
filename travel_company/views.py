from django.shortcuts import render
from django.db.models import Avg
from . import models


def company_list(request):
    companies = models.TourCompany.objects.annotate(
        avg_rating=Avg('reviews__marks')
    )

    return render(request, 'companies.html', {
        'companies': companies
    })