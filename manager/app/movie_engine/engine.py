import requests
from bs4 import BeautifulSoup
from ..models import Movie

def get_random_movie():
    movie = Movie.objects.random()
    data = {
        'title': movie.title,
        'poster': movie.poster
    }
    return data