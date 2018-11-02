import pytest

@pytest.yield_fixture()
def setup():
    print('Running before every Test')
    yield
    print('Running after every Test')


def test_methodA(setup):
    print('Running Method A')


def test_methodB(setup):
    print('Running Method B')


