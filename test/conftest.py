__author__ = 'apavlenko'

import json
import os.path

import pytest

from fixture.application import Application

fixture = None
target = None


@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as f:
            target = json.load(f)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target['baseUrl'])
    fixture.session.ensure_login(username=target['username'], password=target['password'])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    global fixture

    def fin():
        if not fixture is None:
            fixture.session.logout()
            fixture.destroy()

    request.addfinalizer(fin)


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")
