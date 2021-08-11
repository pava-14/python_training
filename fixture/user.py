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
        self.change_field_value("firstname", user.first_name)
        self.change_field_value("middlename", user.middle_name)
        self.change_field_value("lastname", user.last_name)

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

    def get_user_list(self):
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
                # all_phones = cells[5].text.splitlines()
                all_phones = cells[5].text
                # while len(all_phones) < 3:
                #     all_phones.append("None")
                self.user_cache.append(
                    User(first_name=first_name, middle_name=None, last_name=last_name, id=id,
                         all_phones_from_home_page=all_phones))
        return list(self.user_cache)

    def get_user_info_from_edit_page(self, index):
        wd = self.app.wd
        self.edit_user_by_index(index)
        first_name = wd.find_element_by_name("firstname").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        secondary_phone = wd.find_element_by_name("fax").get_attribute("value")
        return User(first_name=first_name, last_name=last_name, id=id, home_phone=home_phone, work_phone=work_phone,
                    mobile_phone=mobile_phone, secondary_phone=secondary_phone)

    def get_user_info_from_view_page(self, index):
        wd = self.app.wd
        self.view_user_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        secondary_phone = re.search("F: (.*)", text).group(1)
        return User(home_phone=home_phone, work_phone=work_phone,
                    mobile_phone=mobile_phone, secondary_phone=secondary_phone)
