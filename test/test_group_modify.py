__author__ = 'apavlenko'

from model.group import Group
import random


def test_modify_group_name(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="Test Group"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    new_group_data = Group(id=group.id, name="Modifyed name", header="Modifyed header", footer="Modifyed footer")
    app.group.modify_group_by_id(group.id, new_group_data)
    new_groups = db.get_group_list()
    old_groups[old_groups.index(group)] = new_group_data
    # update database
    app.user.count()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

def test_modify_group_name(app):
    if app.group.count() == 0:
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

# def test_modify_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="Test Group"))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(header="New header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#
#
# def test_modify_footer(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="Test Group"))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(footer="New footer"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#
#
# def test_group_edit_by_name(app):
#     app.group.modify_by_name("Group_I0KPNM")
