__author__ = 'apavlenko'

import allure
import pytest

from model.contact import Contact
from util.datagenerator import random_firstname, random_short_middlename
from util.datagenerator import random_lastname, random_stret_address
from util.datagenerator import random_email, random_phonenumber


@allure.feature('Contact management (Back)')
@allure.story('Add contact')
@allure.title('Add random contact from json file')
def test_add_contact(app, json_contacts, db, check_ui):
    assert_msg = 'Списки отличаются'
    old_contacts = db.get_contact_list()
    contacts = json_contacts

    app.contact.add_new_wo_group(contacts)

    new_contacts = db.get_contact_list()
    old_contacts.append(contacts)

    assert app.contact.lists_equal(old_contacts, new_contacts), assert_msg

    if check_ui:
        ui_contacts = app.contact.csort(
            app.contact.get_contact_list_from_home_page())
        assert app.contact.lists_equal(ui_contacts, new_contacts), assert_msg


@allure.feature('Contact management (Front)')
@allure.story('Add contact')
@allure.title('Add random contact from json file')
def test_add_contact_wo_group(app, json_contacts):
    assert_msg = 'Списки отличаются'

    old_contacts = app.contact.get_contact_list_from_home_page()

    contacts = json_contacts
    app.contact.add_new_wo_group(contacts)
    new_contacts = app.contact.get_contact_list_from_home_page()

    old_contacts.append(contacts)

    assert app.contact.lists_equal(old_contacts, new_contacts), assert_msg


testdata = [Contact(firstname="", middlename="", lastname="")] + [
    Contact(firstname=random_firstname(), middlename=random_short_middlename(),
            lastname=random_lastname(), address=random_stret_address(),
            f_email=random_email(), s_email=random_email(),
            t_email=random_email(), home_phone=random_phonenumber(),
            mobile_phone=random_phonenumber(),
            work_phone=random_phonenumber())
    for i in range(3)
]


@allure.feature('Contact management (Front)')
@allure.story('Add contact')
@allure.title('Add random contact (parametrize)')
@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact_wo_group_annot(app, contact):
    assert_msg = 'Списки отличаются'
    old_contacts = app.contact.get_contact_list_from_home_page()

    app.contact.add_new_wo_group(contact)
    new_contacts = app.contact.get_contact_list_from_home_page()

    old_contacts.append(contact)

    assert app.contact.lists_equal(old_contacts, new_contacts), assert_msg
