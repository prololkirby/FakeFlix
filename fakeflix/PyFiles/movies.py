from flask import Blueprint, render_template, request, redirect, url_for
import fakeflix.PyFiles.Repository as repo
import fakeflix.PyFiles.services as services
from fakeflix.utilities import utilities
from fakeflix.PyFiles.model import *

movies_blueprint = Blueprint('movies_bp', __name__)


@movies_blueprint.route('/movies', methods=['GET'])
def movies_by_title():
    target_title = request.args.get('title')
    target_year = target_title.release_year
    first_movie = services.get_first_movie(repo.repo_instance)
    last_movie = services.get_last_movie(repo.repo_instance)

    if target_title is None:
        target_title = first_movie['title']
    else:
        target_title = Movie(target_title, target_year)
    movies, prev_title, next_title = services.get_movies_by_title(target_title, target_year, repo.repo_instance)

    first_movie_url = None
    last_movie_url = None
    prev_movie_url = None
    next_movie_url = None

    if len(movies) > 0:
        if prev_title is not None:
            prev_movie_url = url_for('movies_bp.movies_by_title', title = prev_title)
            first_movie_url = url_for('movies_bp.movies_by_title', title = first_movie['title'])
        if next_title is not None:
            next_movie_url = url_for('movies_bp.movies_by_title', title = next_title)
            last_movie_url = url_for('movies_bp.movies_by_title', title = last_movie['title'])
        return render_template('movies/movies.html',
                               title = 'Movies',
                               movies_title = target_title,
                               release_year= target_year,
                               movies = movies,
                               selected_movies = utilities.get_selected_movies(len(movies) * 2),
                               first_movie_url = first_movie_url,
                               last_movie_url = last_movie_url,
                               prev_movie_url = prev_movie_url,
                               next_movie_url = next_movie_url
                               )
    return redirect(url_for('home_bp.home'))
