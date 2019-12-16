from django.contrib import admin
from .models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'language', 'status', 'year_of_production', 'views_count')
    list_display_links = ('id', 'title')
    list_per_page = 10
    search_fields = ('title', 'description')
    list_filter = ('category', 'language', 'status', 'year_of_production', 'views_count')


admin.site.register(Movie, MovieAdmin)
