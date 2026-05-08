from django.shortcuts import render
from django.db.models import Avg
from . import models
from .models import TourCompany


def company_list(request):
    companies = TourCompany.objects.annotate(
        avg_rating=Avg('reviews__marks')
    )

    return render(request, 'companies.html', {
        'companies': companies
    })


def company_list(request):
    companies = models.TourCompany.objects.annotate(
        avg_rating=Avg('reviews__marks')
    )

    return render(request, 'companies.html', {
        'companies': companies
    })