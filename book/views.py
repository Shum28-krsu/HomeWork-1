from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator

from . import models


def search_view(request):

    query = request.GET.get('s', '')

    if query:

        books = models.Book.objects.filter(
            title__icontains=query
        )

        paginator = Paginator(books, 3)

        page_number = request.GET.get('page')

        page_obj = paginator.get_page(page_number)

        return render(
            request,
            'books/book_list.html',
            {
                'page_obj': page_obj
            }
        )

    return HttpResponse('Книга не найдена')




# HOMEWORK 2

def book_list(request):

    books = models.Book.objects.all()

    paginator = Paginator(books, 3)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'books/book_list.html',
        {
            'page_obj': page_obj
        }
    )


def book_detail(request, id):

    book = get_object_or_404(
        models.Book,
        id=id
    )

    # просмотры
    book.views_count += 1
    book.save()

    return render(
        request,
        'books/book_detail.html',
        {
            'book': book
        }
    )