__author__ = 'apavlenko'

import random

from model.user import User


def test_modify_user_db(app, db, check_ui):
    if app.user.count() == 0:
        app.user.add_new_wo_group(User(firstname=app.firstname, middlename=app.middlename, lastname=app.lastname))
    old_users = db.get_contact_list()
    user = random.choice(old_users)
    new_user_data = User(id=user.id, firstname="Modifyed firstname", middlename="Modifyed middlename",
                lastname="Modifyed lastname")
    app.user.modify_user_by_id(user.id, new_user_data)
    new_users = db.get_contact_list()
    #
    # temp_index = old_users.index(user)
    # temp_user = old_users[old_users.index(user)]
    #
    old_users[old_users.index(user)] = user
    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)
    if check_ui:
        assert sorted(new_users, key=User.id_or_max) == sorted(app.user.get_user_list_from_home_page(),
                                                               key=User.id_or_max)


def test_modify_user_by_index(app):
    if app.user.count() == 0:
        app.user.add_new_wo_group(User(firstname=app.firstname, middlename=app.middlename, lastname=app.lastname))
    old_users = app.user.get_user_list_from_home_page()
    index = randrange(len(old_users))
    user = User(firstname="New User", middlename="New User", lastname="New User")
    user.id = old_users[index].id
    app.user.modify_user_by_index(index, user)
    new_users = app.user.get_user_list_from_home_page()
    assert len(old_users) == len(new_users)
    old_users[index] = user
    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)
