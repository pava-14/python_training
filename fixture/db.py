__author__ = 'apavlenko'

import mysql.connector
import allure
from model.contact import Contact
from model.group import Group


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name,
                                                  user=user, password=password,
                                                  autocommit=True)

    @allure.step('Get group list from database')
    def get_group_list(self):
        grouplist = []
        cursor = self.connection.cursor()
        sqlstring = ("SELECT group_id, group_name, group_header, group_footer "
                     "FROM group_list")
        try:
            cursor.execute(sqlstring)
            for row in cursor:
                (id, name, header, footer) = row
                grouplist.append(Group(id=str(id), name=name, header=header,
                                       footer=footer))
        finally:
            cursor.close()
        return grouplist

    @allure.step('Get contact list from database')
    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        sqlstring = ("SELECT id, firstname, middlename, lastname "
                     "FROM addressbook WHERE deprecated IS NULL")
        try:
            cursor.execute(sqlstring)
            for row in cursor:
                (id, firstname, middlename, lastname) = row
                list.append(Contact(id=str(id), firstname=firstname,
                                    middlename=middlename, lastname=lastname))
        finally:
            cursor.close()
        return list

    @allure.step('Get Id contact by group Id')
    def get_id_contacts_by_group_id(self, group_id):
        list = []
        cursor = self.connection.cursor()
        sqlstring = ("SELECT id FROM address_in_groups "
                     f"WHERE (group_id={group_id}) AND "
                     "(id IN (SELECT id FROM addressbook "
                     "WHERE deprecated IS NULL))")
        try:
            cursor.execute(sqlstring)
            for row in cursor:
                (user_id) = row
                list.append(str(user_id[0]))
        finally:
            cursor.close()
        return list

    @allure.step('Get Id not empty group')
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

    @allure.step('Close database connection')
    def destroy(self):
        self.connection.close()
