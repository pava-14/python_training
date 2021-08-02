import pytest

from fixture.application import Application
from fixture.group import GroupHelper
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_group_add(app):
    app.session.login(user_name=app.user_name, user_pass=app.user_pass)
    app.group.create(Group(name=app.group_name, header=app.group_header,
                           footer=app.group_footer))
    # TODO: Check for group_name
    # do something
    app.session.logout()


def test_empty_group_add(app):
    app.session.login(user_name=app.user_name, user_pass=app.user_pass)
    app.group.create(Group(name="", header="", footer=""))
    # TODO: Check for group_name
    # do something
    app.session.logout()
