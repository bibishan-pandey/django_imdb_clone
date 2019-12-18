from django.views.generic import ListView, DetailView
from django.views.generic.dates import YearArchiveView

from .models import Movie, MovieLink
from django.db.models import Q


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
        links = MovieLink.objects.filter(movie=self.get_object())
        embedded_id = self.strip_url(links=list(links.values()))
        context = {
            'movie': super(MovieDetail, self).get_object(),
            'links': links,
            'embedded_id': embedded_id,
            'related_movies': Movie.objects.filter(category=self.get_object().category)#.order_by['created'][:6]
        }
        print(context['related_movies'])
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


class GenreCategory(ListView):
    model = Movie
    template_name = 'movie/movie_category.html'
    context_object_name = 'movies'
    paginate_by = 5

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.category = None

    def get_queryset(self):
        self.category = self.kwargs.get('category')
        movies = Movie.objects.filter(category=self.category)
        return movies

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GenreCategory, self).get_context_data(**kwargs)

        # sending full category name in the context
        if self.category == 'A':
            context['category'] = 'Action'
        elif self.category == 'C':
            context['category'] = 'Comedy'
        elif self.category == 'D':
            context['category'] = 'Drama'
        elif self.category == 'R':
            context['category'] = 'Romance'
        return context


class LanguageCategory(ListView):
    model = Movie
    template_name = 'movie/movie_category.html'
    context_object_name = 'movies'
    paginate_by = 5

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.category = None

    def get_queryset(self):
        self.category = self.kwargs.get('category')  # currently works with only category field
        movies = Movie.objects.filter(language=self.category)
        print(self.category)
        print(list(movies))
        return movies

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(LanguageCategory, self).get_context_data(**kwargs)
        if self.category == 'EN':
            context['category'] = 'English'
        elif self.category == 'GR':
            context['category'] = 'German'
        return context


class MovieSearch(ListView):
    model = Movie
    template_name = 'movie/movie_list.html'
    context_object_name = 'movies'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            object_list = Movie.objects.filter(
                Q(title__icontains=query) |
                Q(cast__icontains=query)
            )
        else:
            object_list = self.model.objects.none()
        return object_list


class MovieYear(YearArchiveView):
    model = Movie
    queryset = Movie.objects.all()
    date_field = 'year_of_production'
    template_name = 'movie/movie_list.html'
    context_object_name = 'movies'
    make_object_list = True
    allow_future = True
    paginate_by = 5
