from flask import Blueprint, render_template, request, redirect, url_for
import fakeflix.PyFiles.Repository as repo
import fakeflix.PyFiles.services as services
#from fakeflix.utilities import utilities
from fakeflix.PyFiles.model import *

movies_blueprint = Blueprint('movies_bp', __name__)


@movies_blueprint.route('/movies', methods=['GET'])
def movies_by_year():
    movies_per_page = 10
    
    cursor = request.args.get('cursor')

    if cursor is None:
        cursor = 0
    else:
        cursor = int(cursor)

    movies = services.get_all_movies(repo.repo_instance)
    select_movies = movies[cursor:cursor+movies_per_page]
    
    next_movies_url = None
    prev_movies_url = None

    if cursor > 0:
        prev_movies_url = url_for('movies_bp.movies_by_year', cursor=cursor - movies_per_page)

    if cursor + movies_per_page < len(movies):
        # There are further articles, so generate URLs for the 'next' and 'last' navigation buttons.
        next_movies_url = url_for('movies_bp.movies_by_year', cursor=cursor + movies_per_page)
            
    return render_template(
        'movies/movies.html',
        title='Movies',
        movies=select_movies,
        next_movies_url=next_movies_url,
        prev_movies_url=prev_movies_url
        )