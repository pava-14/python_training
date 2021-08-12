__author__ = 'apavlenko'

from model.user import User


def test_add_user_wo_group(app):
    old_users = app.user.get_user_list_from_home_page()
    user = User(first_name=app.first_name, middle_name=app.middle_name, last_name=app.last_name)
    app.user.add_new_wo_group(user)
    new_users = app.user.get_user_list_from_home_page()
    assert len(old_users) + 1 == len(new_users)
    old_users.append(user)
    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)
