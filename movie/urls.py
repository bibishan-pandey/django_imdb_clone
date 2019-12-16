from django.urls import path
from . import views

urlpatterns = [
    path('', views.MovieList.as_view(), name='movies'),
    path('<int:pk>/', views.MovieDetail.as_view(), name='detail'),
]
