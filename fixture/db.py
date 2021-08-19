__author__ = 'apavlenko'

import mysql.connector

from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password,
                                                  autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        # self.get_contacts_count()
        list = []
        cursor = self.connection.cursor()
        try:
            # cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00'")
            cursor.execute("select id, firstname, middlename, lastname from addressbook where deprecated is null")
            for row in cursor:
                (id, firstname, middlename, lastname) = row
                list.append(Contact(id=str(id), firstname=firstname, middlename=middlename, lastname=lastname))
        finally:
            cursor.close()
        return list

    def get_id_contacts_by_group_id(self, group_id):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                f"SELECT id FROM address_in_groups WHERE (group_id={group_id}) AND (id IN (SELECT id FROM addressbook WHERE deprecated IS NULL))")
            for row in cursor:
                (user_id) = row
                list.append(str(user_id[0]))
        finally:
            cursor.close()
        return list

    def get_id_not_empty_groups(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "SELECT group_id FROM address_in_groups GROUP BY group_id")
            for row in cursor:
                (group_id) = row
                list.append(str(group_id[0]))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
