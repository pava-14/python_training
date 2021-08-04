__author__ = 'apavlenko'

from model.group import Group


def test_modify_group_name(app):
    app.session.login(user_name=app.user_name, user_pass=app.user_pass)
    app.group.modify_first_group(Group(name="New group"))
    app.session.logout()


def test_modify_header(app):
    app.session.login(user_name=app.user_name, user_pass=app.user_pass)
    app.group.modify_first_group(Group(header="New header"))
    app.session.logout()


def test_modify_footer(app):
    app.session.login(user_name=app.user_name, user_pass=app.user_pass)
    app.group.modify_first_group(Group(footer="New footer"))
    app.session.logout()
