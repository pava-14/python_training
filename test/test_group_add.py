__author__ = 'apavlenko'

from model.group import Group


def test_group_add(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name=app.group_name, header=app.group_header,
                           footer=app.group_footer))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


def test_empty_group_add(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
