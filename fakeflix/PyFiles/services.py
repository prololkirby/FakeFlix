from typing import Iterable

from fakeflix.PyFiles.Repository import AbstractRepository
from fakeflix.PyFiles.model import *


class NonExistentMovieException(Exception):
    pass

def get_first_movie(repo: AbstractRepository):
    movie = repo.get_first_movie()
    return movie_to_dict(movie)

def get_last_movie(repo: AbstractRepository):
    movie = repo.get_last_movie()
    return movie_to_dict(movie)

def get_movies_by_year(year,repo: AbstractRepository):
    movies = repo.get_movies_by_year(target_year=year)
    movies_dto = list()
    prev_year=next_year=None
    if len(movies) >0:
        prev_year = repo.get_prev_year(movies[1])
        next_year = repo.get_next_year(movies[1])
        movies_dto = movies_to_dict(movies)
    return movies_dto, prev_year, next_year


def get_all_movies(repo: AbstractRepository):
    movies = repo.get_all_movies()
    return movies_to_dict(movies)


def movie_to_dict(movie: Movie):
    movie_dict = {'title': movie.title, 'release_year': movie.release_year}
    return movie_dict


def movies_to_dict(movies: Iterable[Movie]):
    return[movie_to_dict(movie) for movie in movies]


def dict_to_movie(dict):
    movie = Movie(dict.title, dict.release_year)
    return movie

