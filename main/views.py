from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


def index(request):
    return render(request, 'main/index.html')


def book_list(request):
    return render(request, 'main/books.html')