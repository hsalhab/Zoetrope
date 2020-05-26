import requests
from bs4 import BeautifulSoup
from ..models import Movie

def get_random_movie():
    movie = Movie.objects.random()
    poster = get_poster_link(movie.imdbid)
    data = {
        'title': movie.title,
        'poster': movie.poster
    }
    return data