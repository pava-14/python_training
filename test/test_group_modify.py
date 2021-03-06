__author__ = 'apavlenko'

import random

from model.group import Group


def test_modify_group_name_db(app, db, check_ui):
    old_groups = db.get_group_list()
    if len(old_groups) == 0:
        app.group.create(Group(name="Test Group"))
        old_groups = db.get_group_list()
    group = random.choice(old_groups)
    new_group_data = Group(id=group.id, name="Modifyed name", header="Modifyed header", footer="Modifyed footer")
    app.group.modify_group_by_id(group.id, new_group_data)
    new_groups = db.get_group_list()
    old_groups[old_groups.index(group)] = new_group_data
    # TODO: update database?
    app.contact.count()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_modify_group_name(app):
    old_groups = app.group.get_group_list()
    if len(old_groups) == 0:
        app.group.create(Group(name="Test Group"))
        old_groups = app.group.get_group_list()
    index = random.randrange(len(old_groups))
    group = Group(name="New group")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
