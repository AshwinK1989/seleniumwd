import pytest


@pytest.fixture()
def setup():
    print('This is a setup method running')


def test_methodA(setup):
    print('Running method A')


def test_methodB():
    print('Running method B')






