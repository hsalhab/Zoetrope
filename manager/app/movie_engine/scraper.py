import pandas as pd
import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine, text
import time
import re

engine = create_engine('sqlite:///movies.db', echo=False)

def load_data():
	movies = pd.read_csv("ml-latest-small/movies.csv", index_col=0)
	ratings = pd.read_csv("ml-latest-small/ratings.csv")
	links = pd.read_csv("ml-latest-small/links.csv", index_col=0, dtype={"imdbId": str})

	return movies, ratings, links

def get_poster_link(imdb_id):
    global total, count, start
    imdb_link = "https://www.imdb.com/title/tt" + imdb_id
    eta = (((time.time() - start) / count) * (total - count)) / 60.0
    print("crawling movie {} out of {}. Time remaining: {} minutes".format(count, total, eta))
    count += 1
    try:
        imdb_page = requests.get(imdb_link)
        soup = BeautifulSoup(imdb_page.text, 'html.parser')
        return soup.select("div[class=poster] > a > img")[0]["src"]
    except:
        return ""

def get_year(title):
    pattern = re.compile('\([0-2][0-9][0-9][0-9]\)')
    title = title.strip().split(' ')
    if pattern.match(title[-1]):
        year = int(title[-1][1:-1])
    else:
        year = None
    return year

def scrape_posters():
    global total, count, start
    movies, _, links = load_data()
    links = links['imdbId']
    movie_links = movies.join(links)
    movie_links['year'] = movie_links['title'].apply(get_year)
    movie_links = movie_links[movie_links['year'].notna()]
    movie_links = movie_links[movie_links['year'] > 2000]
    movie_links['year'] = movie_links['year'].astype('int32')

    total = len(movie_links.index)
    print(total)

    count = 1

    start = time.time()
    movie_links["poster"] = movie_links['imdbId'].apply(get_poster_link)

    movie_links.to_sql('movies', con=engine)

def normalize_titles():
    def normalize(title):
        title_list = title.split('(')
        tmp_title = title_list[0].strip()
        if tmp_title[len(tmp_title) - 5: len(tmp_title)] == ', The':
            tmp_title = 'The ' + tmp_title[:len(tmp_title) - 5] + ' (' + title_list[1]
            print("converted {} to {}".format(title, tmp_title))
        return tmp_title
    
    movie_links = pd.read_sql('select * from movies;', con=engine)
    movie_links['title'] = movie_links['title'].apply(normalize)
    sql = text('DROP TABLE movies;')
    engine.execute(sql)
    movie_links.to_sql('movies', con=engine)

normalize_titles()