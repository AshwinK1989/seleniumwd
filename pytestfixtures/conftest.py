import pytest


@pytest.yield_fixture()
def setup():
    print('Running before every Test')
    yield
    print('Running after every Test')


@pytest.yield_fixture(scope='module')
def one_time_setup(browser, os_type):
    print('Running Once before all Tests')
    if browser == 'firefox':
        print('Running Firefox Browser')
    elif browser == 'Chrome':
        print('Running Chrome Browser')
    yield
    print('Running Once after all Tests')


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Please specify os Type")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def os_type(request):
    return request.config.getoption("--osType")

