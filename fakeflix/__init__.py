import os

from flask import Flask

from .PyFiles.MemoryRepository import *
import fakeflix.PyFiles.Repository as repo


def create_app(test_config=None):
    app = Flask(__name__)

    app.config.from_object('config.Config')
    data_path = os.path.join('fakeflix','datafilereaders','data')

    if test_config is not None:
        app.config.from_mapping(test_config)
        data_path = app.config['TEST_DATA_PATH']
    repo.repo_instance = MemoryRepository()
    populate(data_path, repo.repo_instance)

    with app.app_context():
        from fakeflix.PyFiles import home
        app.register_blueprint(home.home_blueprint)

        from fakeflix.PyFiles import movies
        app.register_blueprint(movies.movies_blueprint)

        #from fakeflix.utilities import utilities
        #app.register_blueprint(utilities.utilities_blueprint)

    return app
