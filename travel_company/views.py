from django.views.generic import ListView
from django.db.models import Avg, Q

from . import models


class CompanyListView(ListView):
    model = models.TourCompany
    template_name = 'companies.html'
    context_object_name = 'page_obj'
    paginate_by = 3

    def get_queryset(self):
        return models.TourCompany.objects.annotate(
            avg_rating=Avg('reviews__marks')
        )


class CompanySearchView(ListView):
    model = models.TourCompany
    template_name = 'companies.html'
    context_object_name = 'page_obj'
    paginate_by = 3

    def get_queryset(self):
        query = self.request.GET.get('s', '')

        return models.TourCompany.objects.filter(
            Q(name__icontains=query) |
            Q(services__name__icontains=query)
        ).annotate(
            avg_rating=Avg('reviews__marks')
        ).distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('s', '')
        return context