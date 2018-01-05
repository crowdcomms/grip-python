import pytest
from grip.client import GRIPClient


@pytest.fixture(scope='session')
def api_key():
    return '1b45f90xbad938c5cf5d48807dr4a918'


@pytest.fixture(scope='session')
def container_id():
    return 16234


@pytest.fixture(scope='function')
def grip_client(api_key):
    return GRIPClient(api_key=api_key)


@pytest.fixture(scope='function')
def grip_test_client(api_key):
    return GRIPClient(api_key=api_key, test_mode=True)
