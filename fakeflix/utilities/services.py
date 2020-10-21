from typing import Iterable
from PyFiles.model import *


def movies_to_dict(movies: Iterable[Movie]):
    return [movie_to_dict(movie) for movie in movies]


def movie_to_dict(movie: Movie):
    movie_dict = {'title': movie.title, 'release_year': movie.release_year}
    return movie_dict
