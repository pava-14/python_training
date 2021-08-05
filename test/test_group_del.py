__author__ = 'apavlenko'

from model.group import Group


def test_group_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test Group"))
    app.group.delete_first()


def test_group_delete_by_name(app):
    app.group.delete_by_name("Group_8E9JTK_edited")
