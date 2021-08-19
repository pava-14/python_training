__author__ = 'apavlenko'

import re

from fixture.orm import ORMFixture
from model.user import User


def test_home_page_data_equal_database_data_orm(app):
    db = ORMFixture(host="localhost", name="addressbook", user="root", password="")
    home_page_contacts_list = app.user.get_user_list_from_home_page()
    database_contacts_list = db.get_contact_list()
    assert sorted(home_page_contacts_list, key=User.id_or_max) == sorted(database_contacts_list, key=User.id_or_max)


def test_home_page_data_equal_database_data_db(app, db):
    home_page_contacts_list = app.user.get_user_list_from_home_page()
    database_contacts_list = db.get_contact_list()
    assert sorted(home_page_contacts_list, key=User.id_or_max) == sorted(database_contacts_list, key=User.id_or_max)


def test_user_home_page_data_equal_user_edit_page(app):
    contact_from_home_page = app.user.get_user_list_from_home_page()[0]
    contact_from_edit_page = app.user.get_user_info_from_edit_page(0)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones == merge_phones_like_on_home_page(contact_from_edit_page)


def test_user_home_page_data_equal_user_view_page(app):
    contact_from_home_page = app.user.get_user_list_from_home_page()[0]
    contact_from_view_page = app.user.get_user_info_from_view_page(0)
    assert contact_from_home_page.firstname == contact_from_view_page.firstname
    assert contact_from_home_page.lastname == contact_from_view_page.lastname
    assert contact_from_home_page.address == contact_from_view_page.address
    assert contact_from_home_page.all_emails == contact_from_view_page.all_emails
    assert contact_from_home_page.all_phones == contact_from_view_page.all_phones


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(user):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [user.home_phone, user.mobile_phone, user.work_phone,
                                                                 user.secondary_phone]))))


def merge_emails_like_on_home_page(user):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [user.f_email, user.s_email, user.t_email]))))
