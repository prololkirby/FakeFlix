from flask import Blueprint

import fakeflix.PyFiles.Repository as repo
import fakeflix.utilities.services as services


# Configure Blueprint.
utilities_blueprint = Blueprint(
    'utilities_bp', __name__)


def get_selected_movies(quantity = 3):
    movies = services.get_movies(quantity, repo.repo_instance)
    return movies

