import requests
from bs4 import BeautifulSoup
from ..models import Movie

def get_poster_link(imdb_link):
    imdb_link = "https://www.imdb.com/title/tt" + imdb_link
    try:
        imdb_page = requests.get(imdb_link)
        soup = BeautifulSoup(imdb_page.text, 'html.parser')
        return soup.select("div[class=poster] > a > img")[0]["src"]
    except:
        return ""

def get_random_movie():
    movie = Movie.objects.random()
    poster = get_poster_link(movie.imdbid)
    data = {
        'title': movie.title,
        'poster': poster
    }
    return data