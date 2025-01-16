from django.shortcuts import render, get_object_or_404
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

from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .models import Musician, Category
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


# def show_category(request, cat_slug):
#    category = get_object_or_404(Category, slug=cat_slug)
#    return render(request, 'main/index.html')
