__author__ = 'apavlenko'

from random import randrange

from model.user import User


def test_delete_some_user(app):
    if app.user.count() == 0:
        app.user.add_new_wo_group(User(first_name=app.first_name, middle_name=app.middle_name, last_name=app.last_name))
    old_users = app.user.get_user_list_from_home_page()
    index = randrange(len(old_users))
    app.user.delete_user_by_index(index)
    new_users = app.user.get_user_list_from_home_page()
    assert len(old_users) - 1 == len(new_users)
    old_users[index:index + 1] = []
    assert old_users == new_users


def test_user_delete_by_full_name(app):
    first_name = "Bob_8GQOOY"
    last_name = "Marley_8GQOOY"
    app.user.delete_by_name(first_name, last_name)
