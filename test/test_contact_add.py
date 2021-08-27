__author__ = 'apavlenko'

import pytest

from model.contact import Contact
from util.datagenerator import *


def test_add_contact(app, json_contacts, db, check_ui):
    old_contacts = db.get_contact_list()
    contacts = json_contacts
    app.contact.add_new_wo_group(contacts)
    new_contacts = db.get_contact_list()
    old_contacts.append(contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list_from_home_page(),
                                                                     key=Contact.id_or_max)


def test_add_contact_wo_group(app, json_contacts):
    old_contacts = app.contact.get_contact_list_from_home_page()
    contacts = json_contacts
    app.contact.add_new_wo_group(contacts)
    new_contacts = app.contact.get_contact_list_from_home_page()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


testdata = [Contact(firstname="", middlename="", lastname="")] + [
    Contact(firstname=random_firstname(), middlename=random_short_middlename(), lastname=random_lastname(),
            address=random_stret_address(),
            f_email=random_email(), s_email=random_email(), t_email=random_email(),
            home_phone=random_phonenumber(), mobile_phone=random_phonenumber(), work_phone=random_phonenumber())
    for i in range(3)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact_wo_group_annot(app, contact):
    old_contacts = app.contact.get_contact_list_from_home_page()
    app.contact.add_new_wo_group(contact)
    new_contacts = app.contact.get_contact_list_from_home_page()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
