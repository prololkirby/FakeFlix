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

    def get_num_of_movies(self):
        return len(self._movies)

    def add_movie(self, movie: Movie):
        self._movies.append(movie)

    def get_all_movies(self):
        return self._movies


def load_movies(data_path: str, repo: MemoryRepository):
    for data_row in read_csv_file(os.path.join(data_path, 'Data1000Movies.csv')):
        number_of_tags = len(data_row)-12
        movie = Movie(
            title=data_row[1],
            release_year=int(data_row[6])
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