__author__ = 'apavlenko'

import random

from model.group import Group


def test_delete_some_group(app, db, check_ui):
    old_groups = db.get_group_list()
    if len(old_groups) == 0:
        app.group.create(Group(name="Test Group"))
        old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_delete_first_group(app):
    old_groups = app.group.get_group_list()
    if len(old_groups) == 0:
        app.group.create(Group(name="Test Group"))
        old_groups = app.group.get_group_list()
    app.group.delete_first()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups
