from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('books', views.book_list, name='books'),
    path('post/<slug:post_slug>/', views.show_post, name='post'),
    #path('category/<slug:cat_slug>/', views.show_category, name='category')
]