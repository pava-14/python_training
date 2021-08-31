__author__ = 'apavlenko'

import random

from pytest_bdd import given, when, then

from model.contact import Contact


@given('a contact list', target_fixture='contact_list')
def get_contact_list(db):
    return db.get_contact_list()


@given('a contact with <firstname> and <lastname>', target_fixture='contact')
def get_contact(firstname, lastname):
    return Contact(firstname=firstname, lastname=lastname)


@when('I add the contact to the list')
def add_contact_to_list(app, contact):
    app.contact.add_new_wo_group(contact)


@then('the new contact list is equal to the old list with the added contact')
def verify_contact_added(contact_list, contact, db):
    old_contact_list = contact_list
    new_contact_list = db.get_contact_list()
    old_contact_list.append(contact)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)


@given('a non-empty contact list', target_fixture='non_empty_contact_list')
def get_non_enpty_contact_list(db, app):
    contact_list = db.get_contact_list()
    if len(contact_list) == 0:
        app.contact.add_new_wo_group(Contact(firstname='firstname11', lastname='lastname11'))
        contact_list = db.get_contact_list()
    return contact_list


@given('a random contact from the list', target_fixture='random_contact')
def get_random_contac(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@when('I delete the contact from the list')
def delete_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.id)


@then('the new contact list is equal to the old list without the deleted contact')
def verify_contact_deleted(db, non_empty_contact_list, random_contact):
    old_contact_list = non_empty_contact_list
    new_contact_list = db.get_contact_list()
    old_contact_list.remove(random_contact)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)


@given('a new contact data with <firstname> and <lastname>', target_fixture='new_contact_data')
def get_new_contact_data(random_contact, firstname, lastname):
    return Contact(id=random_contact.id, firstname=firstname, lastname=lastname)


@when('I modify a contact from a list with a new contact data')
def modify_contact(app, new_contact_data):
    app.contact.modify_contact_by_id(new_contact_data.id, new_contact_data)


@then('the new contact list is equal to the old list with modified contact')
def verify_contact_modified(db, non_empty_contact_list, random_contact, new_contact_data):
    old_contacts = non_empty_contact_list
    old_contacts[old_contacts.index(random_contact)] = new_contact_data
    new_contacts = db.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
