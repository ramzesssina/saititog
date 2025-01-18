from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework import generics, viewsets, mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination

from .forms import AddPostForm
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .models import Musician, Category, TagPost
from .serializers import MusicianSerializer


class MusicianAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000


'''class MusicianViewSet(
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet
):
    #queryset = Musician.objects.all()
    serializer_class = MusicianSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if not pk:
            return Musician.objects.all()[:3]

        return Musician.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})'''


class MusicianAPIList(generics.ListCreateAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = MusicianAPIListPagination


class MusicianAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer
    permission_classes = (IsAuthenticated, )
    # authentication_classes = (TokenAuthentication, )


class MusicianAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer
    permission_classes = (IsAdminOrReadOnly, )


# class MusicianAPIView(generics.ListAPIView):
#    queryset = Musician.objects.all()
#    serializer_class = MusicianSerializer


def index(request):
    posts = Musician.objects.all()
    data = {
        'posts': posts,
    }

    return render(request, 'main/index.html', data)

def feedback(request):
    posts = Musician.objects.all()
    data = {
        'posts': posts,
    }
    return render(request, 'main/feedback.html', data)

@login_required
def allposts(request):
    all_posts = Musician.objects.all()
    paginator = Paginator(all_posts, 3)  # Показывать по 3 поста на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data = {
        'posts': page_obj.object_list,  # Отображаем текущие посты
        'page_obj': page_obj,          # Объект пагинации
        'title': 'Все посты',
        'cat_selected': None
    }

    return render(request, 'main/allposts.html', data)


def show_post(request, post_slug):
    post = get_object_or_404(Musician, slug=post_slug)

    data = {
        'title': post.title,
        'post': post,
        'cat_selected': 1,
    }

    return render(request, 'main/post.html', data)


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Musician.objects.filter(cat_id=category.pk)

    paginator = Paginator(posts, 3)  # Показываем по 3 поста на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data = {
        'title': f'Рубрика: {category.name}',
        'posts': page_obj.object_list,
        'page_obj': page_obj,
        'cat_selected': category.pk,
    }
    return render(request, 'main/allposts.html', context=data)

def show_tag_postlist(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.tags.filter(is_published=Musician.Status.PUBLISHED)

    data = {
        'title': f"Тег: {tag.tag}",
        'posts': posts,
        'cat_selected': None,
    }

    return render(request, 'main/allposts.html', context=data)

def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            try:
                Musician.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, "Ошибка добавления поста")
    else:
        form = AddPostForm()

    data = {
        'title': 'Добавление статьи',
        'form': form
    }
    return render(request, 'main/addpage.html', data)

