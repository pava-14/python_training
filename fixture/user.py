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
        wd.find_elements_by_css_selector("[name=entry] [title=Edit]")[index].click()

    def delete_first(self):
        self.delete_by_index(0)
        self.user_cache = None

    def delete_by_index(self, index):
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
                self.user_cache.append(User(first_name=first_name, middle_name=None, last_name=last_name, id=id))
        return list(self.user_cache)

    def delete_by_name(self, first_name, last_name):
        wd = self.app.wd
        selector_text = "input[title='Select ({0} {1})']".format(first_name, last_name)
        wd.find_element_by_css_selector(selector_text).click()
        wd.find_element_by_css_selector("input[value=Delete]").click()
        wd.switch_to_alert().accept()
        self.user_cache = None
