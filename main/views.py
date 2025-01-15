from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse

from .models import Musician, Category



def index(request):
    return render(request, 'main/index.html')


def book_list(request):
    return render(request, 'main/books.html')

def show_post(request, post_slug):
    post = get_object_or_404(Musician, slug=post_slug)

    data = {
        'title': post.title,
        'post': post,
        'cat_selected': 1,
    }

    return render(request, 'main/post.html', data)

#def show_category(request, cat_slug):
#    category = get_object_or_404(Category, slug=cat_slug)
#    return render(request, 'main/index.html')