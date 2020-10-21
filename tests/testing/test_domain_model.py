from PyFiles.model import *
import pytest


@pytest.fixture()
def movie():
    return Movie("Guardians of The Galaxy", 2014)


def test_movie_construction(movie):
    assert movie.title == "Split"
    assert movie.release_year == 2016
    assert repr(movie) == "(Split, 2016)"


def test_less_than_operator():
    movie1 = Movie("Mary Poppins", 1987)
    movie2 = Movie("Gremlins", 1987)
    assert movie1 < movie2