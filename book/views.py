from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book

# Create your views here.
def quote_a(request):
    return HttpResponse('A lot will go wrong before everything goes right 📽 ')

def quote_b(request):
    return HttpResponse('You are free, and thats why you are lost ☯ ')

def quote_c(request):
    return HttpResponse('Focus on improving yourself , not proving yourself 🧬 ')




#HOMEWORK 2

def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        return render(request, 'books/book_list.html', {'books': books})


def book_detail(request, id):
    if request.method == 'GET':
        book = get_object_or_404(Book, id=id)
        return render(request, 'books/book_detail.html', {'book': book})