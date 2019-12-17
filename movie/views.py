from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Movie, MovieLink


class MovieList(ListView):
    model = Movie
    template_name = 'movie/movie_list.html'
    context_object_name = 'movies'
    paginate_by = 5


class MovieDetail(DetailView):
    model = Movie
    template_name = 'movie/movie_detail.html'

    # retrieve movie links, trailer url and increment view count
    def get_context_data(self, **kwargs):
        # strip youtube trailer link url from 'watch' to 'embed' to avoid
        # 'X-Frame_Options: SAMEORIGIN' in response header from youtube
        links = list(MovieLink.objects.filter(movie=self.get_object()).values())
        embedded_id = self.strip_url(links=links)
        context = {
            'movie': super(MovieDetail, self).get_object(),
            'links': MovieLink.objects.filter(movie=self.get_object()),
            'embedded_id': embedded_id
        }
        context['movie'].views_count += 1  # increments the view count every time a movie object is opened
        context['movie'].save()
        return context

    @staticmethod
    def strip_url(links):
        embedded_url = None
        for link in links:
            if link['link_type'] == 'T':
                stripped_url_list = link['link'].split('/')
                embedded_key = stripped_url_list[-1]
                embedded_key_stripped_list = embedded_key.split('=')
                embedded_url = embedded_key_stripped_list[-1]
        return embedded_url
