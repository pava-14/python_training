__author__ = 'apavlenko'

import pytest

from fixture.application import Application

fixture = None


@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
    else:
        if not fixture.is_valid():
            fixture = Application()
    fixture.session.login(user_name="admin", user_pass="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    global fixture

    def fin():
        fixture.session.logout()
        fixture.destroy()

    request.addfinalizer(fin)
