from django.contrib import admin
from .models import Movie, MovieLink


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'language', 'status', 'cast', 'year_of_production', 'views_count')
    list_display_links = ('id', 'title')
    list_per_page = 10
    search_fields = ('title', 'description', 'cast')
    list_filter = ('category', 'language', 'status', 'year_of_production', 'views_count')


class MovieLinkAdmin(admin.ModelAdmin):
    list_display = ('movie', 'link_type', 'link')
    list_display_links = ('movie', 'link_type', 'link')
    list_per_page = 10
    search_fields = ('movie', 'link_type', 'link')
    list_filter = ('link_type',)


admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieLink, MovieLinkAdmin)
