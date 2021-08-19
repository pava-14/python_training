__author__ = 'apavlenko'

import random


def test_add_contact_to_group(app, db):
    contact = random.choice(db.get_contact_list())
    group = random.choice(db.get_group_list())
    app.contact.add_contact_to_group(contact, group)
    # debug:
    print(f"\nContact: {contact.id} {contact.firstname} {contact.lastname} Added to group: {group.id} {group.name} ")
    group_contacts = db.get_id_contacts_by_group_id(group.id)
    assert contact.id in group_contacts


def test_delete_contact_from_group(app, db):
    # add contact into group
    contact = random.choice(db.get_contact_list())
    group = random.choice(db.get_group_list())
    app.contact.add_contact_to_group(contact, group)
    group_contacts = db.get_id_contacts_by_group_id(group.id)
    assert contact.id in group_contacts
    # debug:
    print(f"\nContact: {contact.id} {contact.firstname} {contact.lastname} Added to group: {group.id} {group.name} ")
    # delete contact from group
    app.contact.delete_contact_from_group(contact.id, group.id)
    new_group_contacts = db.get_id_contacts_by_group_id(group.id)
    assert contact.id not in new_group_contacts
