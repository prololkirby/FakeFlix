import os
import pytest

from fakeflix import create_app

from fakeflix.PyFiles.MemoryRepository import MemoryRepository, populate

TEST_DATA_PATH = os.path.join('C:', os.sep, 'Users', 'Admin-Wesley', 'Desktop', 'Uni', 'FakeFlix', 'tests', 'data')
#TEST DATA PATH should be set to the route from C: to the data folder


@pytest.fixture
def in_memory_repo():
    repo = MemoryRepository()
    populate(TEST_DATA_PATH, repo)
    return repo


@pytest.fixture
def client():
    my_app = create_app({
        'TESTING': True,                                # Set to True during testing.
        'TEST_DATA_PATH': TEST_DATA_PATH,               # Path for loading test data into the repository.
        'WTF_CSRF_ENABLED': False                       # test_client will not send a CSRF token, so disable validation.
    })

    return my_app.test_client()

