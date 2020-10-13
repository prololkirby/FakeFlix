from flask import Blueprint, render_template, request, redirect, url_for
import fakeflix.PyFiles.Repository as repo
import fakeflix.PyFiles.services as services
from fakeflix.utilities import utilities
from fakeflix.PyFiles.model import *

movies_blueprint = Blueprint('movies_bp', __name__)


@movies_blueprint.route('/movies', methods=['GET'])
def movies_by_year():
    """
    target_year = request.args.get('release_year')
    first_movie = services.get_first_movie(repo.repo_instance)
    last_movie = services.get_last_movie(repo.repo_instance)
    if target_year is None:
        target_year = first_movie['release_year']
    movies, prev_year, next_year = services.get_movies_by_year(target_year, repo.repo_instance)

    first_movie_url = None
    last_movie_url = None
    next_movie_url = None
    prev_movie_url = None

    if len(movies) > 0:
        if prev_year is not None:
            prev_movie_url = url_for('movies_bp.movies_by_year', year=prev_year)
            first_movie_url = url_for('movies_bp.movies_by_year', year=first_movie['release_year'])

        if next_year is not None:
            next_movie_url = url_for('movies_bp.movies_by_year', year=next_year)
            last_movie_url = url_for('movies_bp.movies_by_year', year=last_movie['release_year'])

    """
    all_movies = services.get_all_movies(repo.repo_instance)

    return render_template('movies/movies.html',
                            title='Movies',
                            movies=all_movies)
