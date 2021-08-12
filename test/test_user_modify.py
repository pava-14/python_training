__author__ = 'apavlenko'

from random import randrange

from model.user import User


def test_modify_user_by_index(app):
    if app.user.count() == 0:
        app.user.add_new_wo_group(User(first_name=app.first_name, middle_name=app.middle_name, last_name=app.last_name))
    old_users = app.user.get_user_list_from_home_page()
    index = randrange(len(old_users))
    user = User(first_name="New User", middle_name="New User", last_name="New User")
    user.id = old_users[index].id
    app.user.modify_user_by_index(index, user)
    new_users = app.user.get_user_list_from_home_page()
    assert len(old_users) == len(new_users)
    old_users[index] = user
    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)
