import tmdb_client
from main import app
import pytest
import requests
from unittest.mock import Mock
from flask import Flask


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


def test_get_single_movie(monkeypatch):
   mock_single_movie = ['Movie']
   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_single_movie
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
   single_movie = tmdb_client.get_single_movie(movie_id="")
   assert single_movie == mock_single_movie

def test_get_movie_images(monkeypatch):
   mock_movie_images = ['image1', 'image2']
   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_movie_images
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
   movie_images = tmdb_client.get_movie_images(movie_id="")
   assert movie_images == mock_movie_images


def test_get_single_movie_cast(monkeypatch):
   mock_single_movie_cast = ['actor1', 'actor2']
   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_single_movie_cast
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
   single_movie_cast = tmdb_client.get_single_movie(movie_id="")
   assert single_movie_cast == mock_single_movie_cast

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


def test_homepage(monkeypatch):
   api_mock = Mock(return_value={'results': []})
   monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

   with app.test_client() as client:
       response = client.get('/')
       assert response.status_code == 200
       api_mock.assert_called_once_with('movie/popular')
