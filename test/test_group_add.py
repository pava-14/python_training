__author__ = 'apavlenko'

import allure

from model.group import Group


# from data.groups import testdata


@allure.feature('Group management (Front)')
@allure.story('Add group')
@allure.title('Add random group')
def test_group_add(app, json_groups):
    group = json_groups
    with allure.step('Given a group list'):
        old_groups = app.group.get_group_list()
    with allure.step('When I add the group to the list'):
        app.group.create(group=group)
    with allure.step('Then the new group list is equal to \
                        the old list with the added group'):
        new_groups = app.group.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


@allure.feature('Group management (Back)')
@allure.story('Add group')
@allure.title('Add random group')
def test_group_add_db(app, db, json_groups, check_ui):
    group = json_groups
    with allure.step('Given a group list'):
        old_groups = db.get_group_list()

    with allure.step('When I add the group to the list'):
        app.group.create(group)

    with allure.step('Then the new group list is equal to \
                    the old list with the added group'):
        new_groups = db.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

# def test_group_add(app, data_groups):
#     group = data_groups
#     old_groups = app.group.get_group_list()
#     app.group.create(group)
#     assert len(old_groups) + 1 == app.group.count()
#     new_groups = app.group.get_group_list()
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
#
# @pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
# def test_group_add(app, group):
#     old_groups = app.group.get_group_list()
#     app.group.create(group)
#     assert len(old_groups) + 1 == app.group.count()
#     new_groups = app.group.get_group_list()
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
