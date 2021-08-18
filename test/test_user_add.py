__author__ = 'apavlenko'

import pytest

from model.user import User
from util.datagenerator import *


def test_add_user(app, json_users, db, check_ui):
    old_users = db.get_contact_list()
    user = json_users
    app.user.add_new_wo_group(user)
    new_users = db.get_contact_list()
    old_users.append(user)
    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)
    if check_ui:
        assert sorted(new_users, key=User.id_or_max) == sorted(app.user.get_user_list_from_home_page(),
                                                               key=User.id_or_max)


def test_add_user_wo_group(app, json_users):
    old_users = app.user.get_user_list_from_home_page()
    user = json_users
    app.user.add_new_wo_group(user)
    new_users = app.user.get_user_list_from_home_page()
    assert len(old_users) + 1 == len(new_users)
    old_users.append(user)
    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)


testdata = [User(firstname="", middlename="", lastname="")] + [
    User(firstname=random_firstname(), middlename=random_short_middlename(), lastname=random_lastname(),
         address=random_stret_address(),
         f_email=random_email(), s_email=random_email(), t_email=random_email(),
         home_phone=random_phonenumber(), mobile_phone=random_phonenumber(), work_phone=random_phonenumber())
    for i in range(3)
]


@pytest.mark.parametrize("user", testdata, ids=[repr(x) for x in testdata])
def test_add_user_wo_group_annot(app, user):
    old_users = app.user.get_user_list_from_home_page()
    app.user.add_new_wo_group(user)
    new_users = app.user.get_user_list_from_home_page()
    assert len(old_users) + 1 == len(new_users)
    old_users.append(user)
    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)
