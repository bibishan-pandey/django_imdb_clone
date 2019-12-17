from django.urls import path
from . import views

urlpatterns = [
    path('', views.MovieList.as_view(), name='movies'),
    # path('<int:pk>/', views.MovieDetail.as_view(), name='detail'),
    # path('category/<str:category>/', views.MovieCategory.as_view(), name='category'),
    path(r'^(?P<int:pk>\d+/', views.MovieDetail.as_view(), name='detail'),
    path(r'^category/(?P<category>\D+)/', views.MovieCategory.as_view(), name='category'),
]
