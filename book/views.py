from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def quote_a(request):
    return HttpResponse('A lot will go wrong before everything goes right 📽 ')

def quote_b(request):
    return HttpResponse('You are free, and thats why you are lost ☯ ')

def quote_c(request):
    return HttpResponse('Focus on improving yourself , not proving yourself 🧬 ')

