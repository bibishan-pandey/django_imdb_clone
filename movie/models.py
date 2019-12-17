from django.db import models
from django.template.defaultfilters import slugify


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
LINK_CHOICES = (
    ('W', 'WATCH LINK'),
    ('D', 'DOWNLOAD LINK'),
    ('T', 'TRAILER LINK'),
)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='movies')
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    cast = models.CharField(max_length=100)
    year_of_production = models.DateField()
    views_count = models.BigIntegerField(default=0)

    slug = models.SlugField(blank=True, null=True)
    # tags

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Movie, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class MovieLink(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_link')
    link_type = models.CharField(choices=LINK_CHOICES, max_length=1)
    link = models.URLField()

    def __str__(self):
        return 'Movie:{} Link Type:{}'.format(self.movie, self.link_type)
