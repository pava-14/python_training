__author__ = 'apavlenko'

import re

from fixture.orm import ORMFixture
from model.contact import Contact


def test_home_page_data_equal_database_data_orm(app):
    if app.contact.count() == 0:
        app.contact.add_new_wo_group(Contact(firstname=app.firstname, middlename=app.middlename, lastname=app.lastname))
    db = ORMFixture(host="localhost", name="addressbook", user="root", password="")
    home_page_contacts_list = app.contact.get_contact_list_from_home_page()
    database_contacts_list = db.get_contact_list()
    assert sorted(home_page_contacts_list, key=Contact.id_or_max) == sorted(database_contacts_list,
                                                                            key=Contact.id_or_max)


def test_home_page_data_equal_database_data_db(app, db):
    if app.contact.count() == 0:
        app.contact.add_new_wo_group(Contact(firstname=app.firstname, middlename=app.middlename, lastname=app.lastname))
    home_page_contacts_list = app.contact.get_contact_list_from_home_page()
    database_contacts_list = db.get_contact_list()
    assert sorted(home_page_contacts_list, key=Contact.id_or_max) == sorted(database_contacts_list,
                                                                            key=Contact.id_or_max)


def test_contact_home_page_data_equal_contact_edit_page(app):
    contact_from_home_page = app.contact.get_contact_list_from_home_page()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones == merge_phones_like_on_home_page(contact_from_edit_page)


def test_contact_home_page_data_equal_contact_view_page(app):
    contact_from_home_page = app.contact.get_contact_list_from_home_page()[0]
    contact_from_view_page = app.contact.get_contact_info_from_view_page(0)
    assert contact_from_home_page.firstname == contact_from_view_page.firstname
    assert contact_from_home_page.lastname == contact_from_view_page.lastname
    assert contact_from_home_page.address == contact_from_view_page.address
    assert contact_from_home_page.all_emails == contact_from_view_page.all_emails
    assert contact_from_home_page.all_phones == contact_from_view_page.all_phones


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone, contact.work_phone,
                                        contact.secondary_phone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.f_email, contact.s_email, contact.t_email]))))
