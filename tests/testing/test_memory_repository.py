import pytest
from fakeflix.PyFiles.model import *


def test_repository_can_retrieve_article_count(in_memory_repo):
    number_of_movies = in_memory_repo.get_num_of_movies()
    assert number_of_movies == 1000


def test_repository_can_add_movie(in_memory_repo):
    movie = Movie("Bilbo Baggins", int(2020))
    in_memory_repo.add_movie(movie)

