from typing import Iterable

from fakeflix.PyFiles.Repository import AbstractRepository
from fakeflix.PyFiles.model import *


class NonExistentMovieException(Exception):
    pass


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

