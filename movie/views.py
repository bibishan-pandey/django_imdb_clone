from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Movie


class MovieList(ListView):
    model = Movie
    template_name = 'movie/movie_list.html'
    context_object_name = 'movies'
    paginate_by = 5


class MovieDetail(DetailView):
    model = Movie
    template_name = 'movie/movie_detail.html'
    context_object_name = 'movie'

