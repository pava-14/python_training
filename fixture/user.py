import re

from model.user import User


class UserHelper:
    def __init__(self, app):
        self.app = app

    def add_new_wo_group(self, user):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_user_form(user)
        wd.find_elements_by_css_selector("input[name=submit]")[0].click()
        self.app.return_to_home_page()
        self.user_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_user_form(self, user):
        self.change_field_value("firstname", user.firstname)
        self.change_field_value("middlename", user.middlename)
        self.change_field_value("lastname", user.lastname)
        self.change_field_value("address", user.address)
        self.change_field_value("address", user.address)
        self.change_field_value("home", user.home_phone)
        self.change_field_value("mobile", user.mobile_phone)
        self.change_field_value("work", user.work_phone)
        self.change_field_value("email", user.f_email)
        self.change_field_value("email2", user.s_email)
        self.change_field_value("email3", user.t_email)

    def select_user_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def edit_user_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_css_selector("[name=entry] [title=Edit]")[index].click()

    def view_user_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_css_selector("[name=entry] [title=Details]")[index].click()

    def delete_first(self):
        self.delete_user_by_index(0)
        self.user_cache = None

    def delete_user_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_css_selector("input[value=Delete]").click()
        wd.switch_to_alert().accept()
        self.user_cache = None

    def modify_user_by_index(self, index, new_user_data):
        wd = self.app.wd
        self.app.open_home_page()
        # open modification form
        self.edit_user_by_index(index)
        self.fill_user_form(new_user_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.app.return_to_home_page()
        self.user_cache = None

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    user_cache = None

    def delete_by_name(self, first_name, last_name):
        wd = self.app.wd
        selector_text = "input[title='Select ({0} {1})']".format(first_name, last_name)
        wd.find_element_by_css_selector(selector_text).click()
        wd.find_element_by_css_selector("input[value=Delete]").click()
        wd.switch_to_alert().accept()
        self.user_cache = None

    def get_user_list_from_home_page(self):
        if self.user_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.user_cache = []
            rows = wd.find_elements_by_css_selector("tr[name=entry]")
            for row in rows:
                cells = row.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                last_name = cells[1].text
                first_name = cells[2].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.user_cache.append(
                    User(id=id, firstname=first_name, lastname=last_name,
                         address=address, all_emails=all_emails, all_phones=all_phones))
        return list(self.user_cache)

    def get_user_info_from_edit_page(self, index):
        wd = self.app.wd
        self.edit_user_by_index(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        # name
        first_name = wd.find_element_by_name("firstname").get_attribute("value")
        middle_name = wd.find_element_by_name("middlename").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        # address
        address = wd.find_element_by_name("address").get_attribute("value")
        # phones
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        secondary_phone = wd.find_element_by_name("fax").get_attribute("value")
        # emails
        f_email = wd.find_element_by_name("email").get_attribute("value")
        s_email = wd.find_element_by_name("email2").get_attribute("value")
        t_email = wd.find_element_by_name("email3").get_attribute("value")

        return User(id=id, firstname=first_name, middlename=middle_name, lastname=last_name, address=address,
                    home_phone=home_phone, work_phone=work_phone, mobile_phone=mobile_phone,
                    secondary_phone=secondary_phone,
                    f_email=f_email, s_email=s_email, t_email=t_email)

    def get_user_info_from_view_page(self, index):
        wd = self.app.wd
        self.view_user_by_index(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        content = wd.find_element_by_id("content").text
        list_content = content.splitlines()
        full_name_list = list_content[0].split()
        first_name = full_name_list[0]
        last_name = full_name_list[2]
        address = list_content[1]
        all_emails = "\n".join(list_content[7:])
        phones_list = list_content[3:6]
        all_phones = "\n".join(map(lambda x: re.search('\w:\s(.*)', x).group(1), phones_list))
        return User(id=id, firstname=first_name, lastname=last_name, fullname=list_content[0], address=address,
                    all_phones=all_phones, all_emails=all_emails)
