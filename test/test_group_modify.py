__author__ = 'apavlenko'

from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test Group"))
    app.group.modify_first_group(Group(name="New group"))


def test_modify_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test Group"))
    app.group.modify_first_group(Group(header="New header"))


def test_modify_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test Group"))
    app.group.modify_first_group(Group(footer="New footer"))


def test_group_edit_by_name(app):
    app.group.modify_by_name("Group_I0KPNM")
