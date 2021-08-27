__author__ = 'apavlenko'

import random

from model.contact import Contact


def test_delete_some_contact_db(app, db, check_ui):
    old_contacts = db.get_contact_list()
    if len(old_contacts) == 0:
        app.contact.add_new_wo_group(Contact(firstname=app.firstname, middlename=app.middlename, lastname=app.lastname))
        old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    # TODO: update database
    app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert len(old_contacts) == len(new_contacts)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list_from_home_page(),
                                                                     key=Contact.id_or_max)


def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new_wo_group(Contact(firstname=app.firstname, middlename=app.middlename, lastname=app.lastname))
    old_contacts = app.contact.get_contact_list_from_home_page()
    index = random.randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contact_list_from_home_page()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index:index + 1] = []
    assert old_contacts == new_contacts


def test_contact_delete_by_full_name(app):
    first_name = "Bob_8GQOOY"
    last_name = "Marley_8GQOOY"
    app.contact.delete_by_name(first_name, last_name)
