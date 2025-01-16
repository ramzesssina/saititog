from django.urls import path, include, re_path
from . import views

from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

'''class MyCustomRouter(routers.SimpleRouter):
    routes = [
        routers.Route(url=r'^{prefix}$',
                      mapping={'get': 'list'},
                      name='{basename}-list',
                      detail=False,
                      initkwargs={'suffix': 'List'}),
        routers.Route(url=r'^{prefix}/{lookup}$',
                      mapping={'get': 'retrieve'},
                      name='{basename}-detail',
                      detail=True,
                      initkwargs={'suffix': 'Detail'})
    ]


router = MyCustomRouter()
router.register(r'musician', views.MusicianViewSet, basename="musician")
print(router.urls)'''

urlpatterns = [
    path('', views.index, name='home'),
    path('books', views.book_list, name='books'),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('post/<slug:post_slug>/', views.show_post, name='post'),
    path('api/v1/musician/', views.MusicianAPIList.as_view()),
    path('api/v1/musician/<int:pk>/', views.MusicianAPIUpdate.as_view()),
    path('api/v1/musiciandelete/<int:pk>/', views.MusicianAPIDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
#    path('api/v1/', include(router.urls))
#    path('api/v1/musicianlist/', views.MusicianViewSet.as_view({'get': 'list'})),
#    path('api/v1/musicianlist/<int:pk>/', views.MusicianViewSet.as_view({'put': 'update'})),
 #path('category/<slug:cat_slug>/', views.show_category, name='category')
]