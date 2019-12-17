from django.urls import path
from . import views

urlpatterns = [
    path('', views.MovieList.as_view(), name='home'),
    # path('<int:pk>/', views.MovieDetail.as_view(), name='detail'),
    # path('category/<str:category>/', views.MovieCategory.as_view(), name='category'),
    path(r'^(?P<int:pk>\d+)/', views.MovieDetail.as_view(), name='detail'),
    path(r'^genre category/(?P<category>\D+)/', views.GenreCategory.as_view(), name='genre category'),
    path(r'^language category/(?P<category>\D+)/', views.LanguageCategory.as_view(), name='language category'),
    path(r'^search/', views.MovieSearch.as_view(), name='search'),
]
