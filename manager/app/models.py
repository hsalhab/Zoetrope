from django.db import models
from django.db.models.aggregates import Count
from random import randint

class App(models.Model):
    message = models.CharField(max_length=500, blank=True)

class MovieManager(models.Manager):
    def random(self):
        count = self.aggregate(count=Count('movieid'))['count']
        random_index = randint(0, count - 1)
        return self.all()[random_index]

class Movie(models.Model):
    objects = MovieManager()
    movieid = models.BigIntegerField(db_column='movieId', primary_key=True)
    title = models.TextField(blank=True, null=True)
    genres = models.TextField(blank=True, null=True)
    imdbid = models.TextField(db_column='imdbId', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movies'
