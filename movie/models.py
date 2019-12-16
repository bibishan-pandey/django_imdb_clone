from django.db import models


CATEGORY_CHOICES = (
    ('A', 'ACTION'),
    ('D', 'DRAMA'),
    ('C', 'COMEDY'),
    ('R', 'ROMANCE'),
)
LANGUAGE_CHOICES = (
    ('EN', 'ENGLISH'),
    ('GR', 'GERMAN'),
)
STATUS_CHOICES = (
    ('RA', 'RECENTLY ADDED'),
    ('MW', 'MOST WATCHED'),
    ('TR', 'TOP RATED'),
)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='movies')
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    year_of_production = models.DateField()
    views_count = models.BigIntegerField(default=0)
    # tags
    # watch_links
    # download_links
