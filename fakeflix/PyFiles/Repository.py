import abc
from typing import List

from fakeflix.PyFiles.model import *

repo_instance = None


class RepositoryException(Exception):

    def __init__(self, message=None):
        pass


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def get_user(self, username):
        raise NotImplementedError

    @abc.abstractmethod
    def add_user(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_num_of_movies(self):
        raise NotImplementedError

    @abc.abstractmethod
    def add_movie(self, movie: Movie):
        raise NotImplementedError

    @abc.abstractmethod
    def get_all_movies(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_by_year(self, year):
        raise NotImplementedError

    @abc.abstractmethod
    def get_prev_year(self, movie:Movie):
        raise NotImplementedError

    @abc.abstractmethod
    def get_next_year(self, movie:Movie):
        raise NotImplementedError

    @abc.abstractmethod
    def get_last_movie(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_first_movie(self):
        raise NotImplementedError