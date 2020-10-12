from typing import Iterable
import random
from fakeflix.PyFiles.MemoryRepository import AbstractRepository
from fakeflix.PyFiles.model import *


def get_movies(quantity, repo: AbstractRepository):
    movies_count = repo.get_num_of_movies()
    if quantity >= movies_count:
        quantity = movies_count -1
    random_ids = random.sample(range(1, movies_count), quantity)
    movies = repo.get_movie_by_id(random_ids)
    return movies_to_dict(movies)


def movies_to_dict(movies: Iterable[Movie]):
    return [movies_to_dict(movies) for movie in movies]


def movie_to_dict(movie: Movie):
    movie_dict = {'title': movie.title, 'release_year': movie.release_year}
    return movie_dict
