import pytest
from grip_intros.client import GRIPClient
from grip_intros.container import Container
import os
import json

from grip_intros.thing import Thing

path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'responses')


@pytest.fixture(scope='session')
def api_key():
    return '1b45f90xbad938c5cf5d48807dr4a918'


@pytest.fixture(scope='session')
def container_id():
    return 23


@pytest.fixture(scope='session')
def thing_id():
    return 16


@pytest.fixture(scope='session')
def example_container():
    with open(os.path.join(path, 'test_get_container.json')) as f:
        return Container.from_dict(json.load(f).get('data'))


@pytest.fixture(scope='session')
def example_thing():
    with open(os.path.join(path, 'test_get_thing_detail.json')) as f:
        return Thing.from_dict(json.load(f).get('data'))


@pytest.fixture(scope='function')
def grip_client(api_key):
    return GRIPClient(api_key=api_key)


@pytest.fixture(scope='function')
def grip_test_client(api_key):
    return GRIPClient(api_key=api_key, test_mode=True)
