__author__ = 'apavlenko'

import random

from model.user import User


def test_delete_some_user_db(app, db, check_ui):
    if app.user.count() == 0:
        app.user.add_new_wo_group(User(firstname=app.firstname, middlename=app.middlename, lastname=app.lastname))
    old_users = db.get_contact_list()
    user = random.choice(old_users)
    app.user.delete_user_by_id(user.id)
    # TODO: update database
    app.user.count()
    new_users = db.get_contact_list()
    old_users.remove(user)
    assert len(old_users) == len(new_users)
    assert old_users == new_users
    if check_ui:
        assert sorted(new_users, key=User.id_or_max) == sorted(app.user.get_user_list_from_home_page(),
                                                               key=User.id_or_max)


def test_delete_some_user(app):
    if app.user.count() == 0:
        app.user.add_new_wo_group(User(firstname=app.firstname, middlename=app.middlename, lastname=app.lastname))
    old_users = app.user.get_user_list_from_home_page()
    index = random.randrange(len(old_users))
    app.user.delete_user_by_index(index)
    new_users = app.user.get_user_list_from_home_page()
    assert len(old_users) - 1 == len(new_users)
    old_users[index:index + 1] = []
    assert old_users == new_users


def test_user_delete_by_full_name(app):
    first_name = "Bob_8GQOOY"
    last_name = "Marley_8GQOOY"
    app.user.delete_by_name(first_name, last_name)
