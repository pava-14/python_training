__author__ = 'apavlenko'

import random

from model.contact import Contact


def test_modify_contact_db(app, db, check_ui):
    old_contacts = db.get_contact_list()
    if len(old_contacts) == 0:
        app.contact.add_new_wo_group(Contact(firstname=app.firstname, middlename=app.middlename, lastname=app.lastname))
        old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    new_contact_data = Contact(id=contact.id, firstname="Modifyed firstname", middlename="Modifyed middlename",
                               lastname="Modifyed lastname")
    app.contact.modify_contact_by_id(contact.id, new_contact_data)
    # TODO: update database
    app.contact.count()
    old_contacts[old_contacts.index(contact)] = contact
    new_contacts = db.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list_from_home_page(),
                                                                     key=Contact.id_or_max)


def test_modify_contact_by_index(app):
    old_contacts = app.contact.get_contact_list_from_home_page()
    if len(old_contacts) == 0:
        app.contact.add_new_wo_group(Contact(firstname=app.firstname, middlename=app.middlename, lastname=app.lastname))
        old_contacts = app.contact.get_contact_list_from_home_page()
    index = random.randrange(len(old_contacts))
    contact = Contact(firstname="New Contact", middlename="New Contact", lastname="New Contact")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list_from_home_page()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
