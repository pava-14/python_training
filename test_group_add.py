# ~*~ coding: utf-8 ~*~

import pytest
from application import Application
from group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_group_add(app):
    app.login(user_name=app.user_name, user_pass=app.user_pass)
    app.create_group(Group(name=app.group_name, header=app.group_header,
                           footer=app.group_footer))
    # TODO: Check for group_name
    # do something
    app.logout()


def test_empty_group_add(app):
    app.login(user_name=app.user_name, user_pass=app.user_pass)
    app.create_group(Group(name="", header="", footer=""))
    # TODO: Check for group_name
    # do something
    app.logout()
