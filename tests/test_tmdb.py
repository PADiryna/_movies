import tmdb_client
from main import app
import pytest
import requests
from unittest.mock import Mock

key = 'fab609a99011d2a5301b69f5e86466bc'
token ='eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmYWI2MDlhOTkwMTFkMmE1MzAxYjY5ZjVlODY0NjZiYyIsInN1YiI6IjYzZmJmMDY5ODRmMjQ5MDBhOTQxZjI2NSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ed_rAlbtavSLRvYBlFpfIdzrqLCH3SaujU_s_AKazYc'


def test_get_poster_url_uses_default_size():
   # Підготовка даних
   poster_api_path = "some-poster-path"
   expected_default_size = 'w342'
   # Виклик коду, який ми тестуємо
   poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)
   # Порівняння результатів
   assert expected_default_size in poster_url

def get_popular_movies_movie_num():
   movie_num = 'some-movie=num'
   expected_default_num = '8' 
   popular_movies = tmdb_client. get_popular_movies(movie_num=movie_num)
   return expected_default_num in popular_movies

   # Перевірка функції get_single_movie()
def test_get_single_movie():
   single_movie = tmdb_client.get_single_movie(943822)
   assert single_movie is not None

def test_get_single_movie_cast():
   single_movie_cast = tmdb_client.get_single_movie_cast(943822)
   assert single_movie_cast is not None

def call_tmdb_api(endpoint):
   full_url = f"https://api.themoviedb.org/3/{endpoint}"
   headers = {
       "Authorization": f"Bearer {token}"
   }
   response = requests.get(full_url, headers=headers)
   response.raise_for_status()
   return response.json()

def get_single_movie(movie_id):
   return call_tmdb_api(f"movie/{movie_id}")

