import re

import allure

from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    @allure.step('Add new contact')
    def add_new_wo_group(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text('add new').click()
        self.fill_contact_form(contact)
        wd.find_elements_by_css_selector('input[name=submit]')[0].click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    @allure.step('Fill contact form')
    def fill_contact_form(self, contact):
        self.change_field_value('firstname', contact.firstname)
        self.change_field_value('middlename', contact.middlename)
        self.change_field_value('lastname', contact.lastname)
        self.change_field_value('address', contact.address)
        self.change_field_value('address', contact.address)
        self.change_field_value('home', contact.home_phone)
        self.change_field_value('mobile', contact.mobile_phone)
        self.change_field_value('work', contact.work_phone)
        self.change_field_value('email', contact.f_email)
        self.change_field_value('email2', contact.s_email)
        self.change_field_value('email3', contact.t_email)

    @allure.step('Select contact by index')
    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name('selected[]')[index].click()

    @allure.step('Edit contact by index')
    def edit_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_css_selector('[name=entry] [title=Edit]')[index].click()

    @allure.step('View contact by index')
    def view_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_css_selector('[name=entry] [title=Details]')[index].click()

    @allure.step('Delete first contact')
    def delete_first(self):
        self.delete_contact_by_index(0)
        self.contact_cache = None

    @allure.step('Delete contact by Id')
    def delete_contact_by_id(self, contact_id):
        wd = self.app.wd
        self.select_contact_by_id(contact_id)
        self.delete_selected_contact()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    @allure.step('Delete selected contact')
    def delete_selected_contact(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('input[value=Delete]').click()

    @allure.step('Select contact by Id')
    def select_contact_by_id(self, contact_id):
        wd = self.app.wd
        wd.find_element_by_css_selector(f'input[id="{contact_id}"]').click()

    @allure.step('Delete contact by index')
    def delete_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()
        self.delete_selected_contact()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    @allure.step('Edit contact by Id')
    def edit_contact_by_id(self, contact_id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_css_selector(f'[href="edit.php?id={contact_id}"] [title=Edit]').click()

    @allure.step('Modify contact by Id')
    def modify_contact_by_id(self, contact_id, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        # open modification form
        self.edit_contact_by_id(contact_id)

        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name('update').click()
        self.app.return_to_home_page()
        self.contact_cache = None

    @allure.step('Modify contact by index')
    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        # open modification form
        self.edit_contact_by_index(index)
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name('update').click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name('selected[]'))

    contact_cache = None

    @allure.step('Delete contact by name')
    def delete_by_name(self, first_name, last_name):
        wd = self.app.wd
        selector_text = 'input[title="Select ({0} {1})"]'.format(first_name, last_name)
        wd.find_element_by_css_selector(selector_text).click()
        self.delete_selected_contact()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    @allure.step('Add contact to group')
    def add_contact_to_group(self, contact, group):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(contact.id)
        self.select_group_in_dropdown_by_id(group.id)
        wd.find_element_by_name('add').click()
        self.app.open_home_page()

    @allure.step('Select group in dropdown')
    def select_group_in_dropdown_by_id(self, group_id):
        wd = self.app.wd
        dropdown = wd.find_element_by_name('to_group')
        dropdown.click()
        dropdown.find_element_by_css_selector(f'select[name="to_group"] [value="{group_id}"]').click()

    @allure.step('Delete contact from group')
    def delete_contact_from_group(self, contact_id, group_id):
        wd = self.app.wd
        self.app.group.open_group_property(group_id)
        self.select_contact_by_id(contact_id)
        wd.find_element_by_name('remove').click()

    @allure.step('Get contacts from home page')
    def get_contact_list_from_home_page(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            rows = wd.find_elements_by_css_selector('tr[name=entry]')
            for row in rows:
                cells = row.find_elements_by_tag_name('td')
                contact_id = cells[0].find_element_by_name('selected[]').get_attribute('value')
                last_name = cells[1].text
                first_name = cells[2].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(
                    Contact(id=contact_id, firstname=first_name,
                            lastname=last_name,
                            address=address, all_emails=all_emails,
                            all_phones=all_phones))
        return list(self.contact_cache)

    @allure.step('Get contact info from edit page')
    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.edit_contact_by_index(index)
        id = wd.find_element_by_name('id').get_attribute('value')
        # name
        first_name = wd.find_element_by_name('firstname').get_attribute('value')
        middle_name = wd.find_element_by_name('middlename').get_attribute('value')
        last_name = wd.find_element_by_name('lastname').get_attribute('value')
        # address
        address = wd.find_element_by_name('address').get_attribute('value')
        # phones
        home_phone = wd.find_element_by_name('home').get_attribute('value')
        work_phone = wd.find_element_by_name('work').get_attribute('value')
        mobile_phone = wd.find_element_by_name('mobile').get_attribute('value')
        secondary_phone = wd.find_element_by_name('fax').get_attribute('value')
        # emails
        f_email = wd.find_element_by_name('email').get_attribute('value')
        s_email = wd.find_element_by_name('email2').get_attribute('value')
        t_email = wd.find_element_by_name('email3').get_attribute('value')

        return Contact(id=id, firstname=first_name, middlename=middle_name,
                       lastname=last_name, address=address,
                       home_phone=home_phone, work_phone=work_phone,
                       mobile_phone=mobile_phone,
                       secondary_phone=secondary_phone,
                       f_email=f_email, s_email=s_email, t_email=t_email)

    @allure.step('Get contact info from view page')
    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.view_contact_by_index(index)
        id = wd.find_element_by_name('id').get_attribute('value')
        content = wd.find_element_by_id('content').text
        list_content = content.splitlines()
        full_name_list = list_content[0].split()
        first_name = full_name_list[0]
        last_name = full_name_list[2]
        address = list_content[1]
        all_emails = '\n'.join(list_content[7:])
        phones_list = list_content[3:6]
        all_phones = '\n'.join(map(lambda x: re.search('\w:\s(.*)', x).group(1), phones_list))
        return Contact(id=id, firstname=first_name, lastname=last_name, fullname=list_content[0], address=address,
                       all_phones=all_phones, all_emails=all_emails)

    @allure.step('Sorting contact list')
    def csort(self, contacts):
        return sorted(contacts, key=Contact.id_or_max)

    @allure.step('Check for equals lists')
    def lists_equal(self, fcontacts, scontacts):
        return self.csort(fcontacts) == self.csort(scontacts)
