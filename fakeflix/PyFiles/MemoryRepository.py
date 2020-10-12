import csv
import os
from abc import ABC
from typing import List

from bisect import bisect_left, insort_left

from fakeflix.PyFiles.Repository import AbstractRepository
from fakeflix.PyFiles.model import *


class MemoryRepository(AbstractRepository, ABC):
    def __init__(self):
        self._movies = list()
        self._movies_index = dict()
        self._users = list()

    def add_user(self, user: User):
        self._users.append(user)

    def get_user(self, username) -> User:
        return next((user for user in self._users if user.username == username), None)

    def get_first_movie(self) -> Movie:
        movie = None
        if len(self._movies) > 0:
            movie = self._movies[0]
        return movie

    def get_last_movie(self) -> Movie:
        movie = None
        if len(self._movies) > 0:
            movie = self._movies[-1]
        return movie

    def get_movies_by_title(self, target_title, target_year) -> List[Movie]:
        target_movie = Movie(title=target_title, release_year=target_year)
        matching_movies = list()
        try:
            index = self.movie_index(target_movie)
            for movie in self._movies[index:None]:
                if movie.title == target_title:
                    matching_movies.append(movie)
                else:
                    break
        except ValueError:
            pass
        return matching_movies

    def get_title_of_prev_movie(self, movie: Movie):
        prev_title = None
        try:
            index = self.movie_index(movie)
            for stored_movie in reversed(self._movies[0:index]):
                if stored_movie.title < movie.title:
                    prev_title = stored_movie.title
                    break
        except ValueError:
            pass
        return prev_title

    def get_title_of_next_movie(self, movie: Movie):
        next_title = None
        try:
            index = self.movie_index(movie)
            for stored_movie in self._movies[index+1:len(self._movies)]:
                if stored_movie.title > movie.title:
                    next_title = stored_movie
                    break
        except ValueError:
            pass
        return next_title

    def get_num_of_movies(self):
        return len(self._movies)

    def get_movie_by_id(self, id_list):
        existing_ids = [id for id in id_list if id in self._movies_index]
        movies = [self._movies_index[id] for id in existing_ids]
        return movies

    def movie_index(self, movie: Movie):
        index = bisect_left(self._movies, movie)
        if index != len(self._movies) and self._movies[index].title == movie.title:
            return index
        raise ValueError

    def add_movie(self, movie: Movie):
        insort_left(self._movies, movie)
        self._movies_index[movie.id] = movie

    def get_movie(self, id: int) -> Movie:
        movie = None
        try:
            movie = self._movies_index[id]
        except KeyError:
            pass
        return movie


def load_movies(data_path: str, repo: MemoryRepository):
    for data_row in read_csv_file(os.path.join(data_path, 'Data1000Movies.csv')):
        number_of_tags = len(data_row)-12
        movie = Movie(
            title=data_row[1],
            release_year=int(data_row[6]),
            id = int(data_row[0])
        )
        repo.add_movie(movie)


def read_csv_file(filename: str):
    with open(filename, encoding='utf-8-sig') as infile:
        reader = csv.reader(infile)
        headers = next(reader)
        for row in reader:
            row = [item.strip() for item in row]
            yield row


def populate(data_path: str, repo: MemoryRepository):
    load_movies(data_path, repo)