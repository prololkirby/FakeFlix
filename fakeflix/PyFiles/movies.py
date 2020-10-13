from flask import Blueprint, render_template, request, redirect, url_for
import fakeflix.PyFiles.Repository as repo
import fakeflix.PyFiles.services as services
from fakeflix.utilities import utilities
from fakeflix.PyFiles.model import *

movies_blueprint = Blueprint('movies_bp', __name__)


@movies_blueprint.route('/movies', methods=['GET'])
def movies():
    all_movies = services.get_all_movies(repo.repo_instance)
    return render_template("movies/movies.html",
                           title="Movies",
                           movies=all_movies
                           )
