from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Avg, Q

from .models import TourCompany


def company_list(request):

    companies = TourCompany.objects.annotate(
        avg_rating=Avg('reviews__marks')
    )

    paginator = Paginator(companies, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'companies.html', {
        'page_obj': page_obj
    })


def search_view_c(request):

    query = request.GET.get('s', '')

    companies = TourCompany.objects.filter(
        Q(name__icontains=query) |
        Q(services__name__icontains=query)
    ).annotate(
        avg_rating=Avg('reviews__marks')
    ).distinct()

    paginator = Paginator(companies, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'companies.html', {
        'page_obj': page_obj,
        'query': query
    })