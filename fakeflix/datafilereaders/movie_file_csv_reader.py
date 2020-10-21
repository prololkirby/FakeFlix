import csv

from fakeflix.PyFiles.model import Genre, Director, Actor, Movie


class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self._dataset_of_movies = list()
        self._dataset_of_actors = list()
        self._dataset_of_directors = list()
        self._dataset_of_genres = list()
    @property
    def dataset_of_movies(self):
        return self.dataset_of_movies
    @property
    def dataset_of_actors(self):
        return self.dataset_of_actors
    @property
    def dataset_of_directors(self):
        return self.dataset_of_directors
    @property
    def dataset_of_genres(self):
        return self.dataset_of_genres

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            index = 0
            for row in movie_file_reader:
                title = row['Title']
                genres = row['Genre']
                director = row['Director']
                actors = row['Actors']
                release_year = int(row['Year'])
                index += 1
                movie = Movie(title, release_year)
                self.dataset_of_movies.append(movie)
                genre_list = genres.split(",")
                for genre in genre_list:
                    g = Genre(genre)
                    if g not in self.dataset_of_genres:
                        self.dataset_of_genres.append(g)
                d = Director(director)
                if d not in self.dataset_of_directors:
                    self.dataset_of_directors.append(d)
                actor_list = actors.split(",")
                for actor in actor_list:
                    a = Actor(actor)
                    if a not in self.dataset_of_actors:
                        self.dataset_of_actors.append(a)
filename = 'Data1000Movies.csv'
movie_file_reader = MovieFileCSVReader(filename)
movie_file_reader.read_csv_file()

print(f'number of unique movies: {len(movie_file_reader.dataset_of_movies)}')
print(f'number of unique actors: {len(movie_file_reader.dataset_of_actors)}')
print(f'number of unique directors: {len(movie_file_reader.dataset_of_directors)}')
print(f'number of unique genres: {len(movie_file_reader.dataset_of_genres)}')