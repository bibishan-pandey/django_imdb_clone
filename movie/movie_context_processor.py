from .models import Movie


# add this in settings inside the templates context processor
def slider_movies(request):
    movies = Movie.objects.all().order_by('created')[:]
    return {
        'slider_movies': movies
    }
