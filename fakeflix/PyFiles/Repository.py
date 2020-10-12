import abc
from typing import List

from fakeflix.PyFiles.model import *

repo_instance = None


class RepositoryException(Exception):

    def __init__(self, message=None):
        pass


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def get_first_movie(self) -> Movie:
        raise NotImplementedError

    @abc.abstractmethod
    def get_last_movie(self) -> Movie:
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_by_title(self, target_title, target_year) -> List[Movie]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_title_of_prev_movie(self, movie: Movie):
        raise NotImplementedError

    @abc.abstractmethod
    def get_title_of_next_movie(self, movie: Movie):
        raise NotImplementedError

    @abc.abstractmethod
    def get_num_of_movies(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_by_id(self, id_list):
        raise NotImplementedError

    @abc.abstractmethod
    def movie_index(self, movie: Movie):
        raise NotImplementedError

    @abc.abstractmethod
    def add_movie(self, movie: Movie):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie(self, id: int) -> Movie:
        raise NotImplementedError
