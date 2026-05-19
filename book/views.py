from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from . import models


class BookListView(ListView):
    model = models.Book
    template_name = 'books/book_list.html'
    context_object_name = 'page_obj'
    paginate_by = 3

    def get_queryset(self):
        return models.Book.objects.all()


class SearchView(ListView):
    model = models.Book
    template_name = 'books/book_list.html'
    context_object_name = 'page_obj'
    paginate_by = 3

    def get_queryset(self):
        query = self.request.GET.get('s', '')

        if query:
            return models.Book.objects.filter(
                title__icontains=query
            )

        return models.Book.objects.none()

    def render_to_response(self, context, **response_kwargs):
        if not self.request.GET.get('s'):
            return HttpResponse('Книга не найдена')

        return super().render_to_response(
            context,
            **response_kwargs
        )


class BookDetailView(DetailView):
    model = models.Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'
    pk_url_kwarg = 'id'

    def get_object(self, queryset=None):
        book = super().get_object(queryset)

        book.views_count += 1
        book.save()

        return book