import pytest


def pytest_addoption(parser):
    parser.addoption("--Browser", action="store", default="[chrome, firefox]")


@pytest.fixture
def browsers(request):
    return request.config.getoption("--Browser")