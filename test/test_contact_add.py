__author__ = 'apavlenko'

import pytest

from model.contact import Contact
from util.datagenerator import random_firstname, random_short_middlename
from util.datagenerator import random_lastname, random_stret_address
from util.datagenerator import random_email, random_phonenumber


def test_add_contact(app, json_contacts, db, check_ui):
    old_contacts = db.get_contact_list()
    contacts = json_contacts

    app.contact.add_new_wo_group(contacts)

    new_contacts = db.get_contact_list()
    old_contacts.append(contacts)

    old_sorted = sorted(old_contacts, key=Contact.id_or_max)
    new_sorted = sorted(new_contacts, key=Contact.id_or_max)

    assert old_sorted == new_sorted

    if check_ui:
        contacts_homepage = app.contact.get_contact_list_from_home_page()
        old_sorted = sorted(contacts_homepage, key=Contact.id_or_max)
        assert old_sorted == new_sorted


def test_add_contact_wo_group(app, json_contacts):
    old_contacts = app.contact.get_contact_list_from_home_page()
    contacts = json_contacts

    app.contact.add_new_wo_group(contacts)
    new_contacts = app.contact.get_contact_list_from_home_page()

    assert len(old_contacts) + 1 == len(new_contacts)

    old_contacts.append(contacts)

    old_sorted = sorted(old_contacts, key=Contact.id_or_max)
    new_sorted = sorted(new_contacts, key=Contact.id_or_max)

    assert old_sorted == new_sorted


testdata = [Contact(firstname="", middlename="", lastname="")] + [
    Contact(firstname=random_firstname(), middlename=random_short_middlename(),
            lastname=random_lastname(), address=random_stret_address(),
            f_email=random_email(), s_email=random_email(),
            t_email=random_email(), home_phone=random_phonenumber(),
            mobile_phone=random_phonenumber(),
            work_phone=random_phonenumber())
    for i in range(3)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact_wo_group_annot(app, contact):
    old_contacts = app.contact.get_contact_list_from_home_page()
    app.contact.add_new_wo_group(contact)
    new_contacts = app.contact.get_contact_list_from_home_page()

    assert len(old_contacts) + 1 == len(new_contacts)

    old_contacts.append(contact)

    old_sorted = sorted(old_contacts, key=Contact.id_or_max)
    new_sorted = sorted(new_contacts, key=Contact.id_or_max)

    assert old_sorted == new_sorted
