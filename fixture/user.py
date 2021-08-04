class UserHelper:
    def __init__(self, app):
        self.app = app

    def add_new_wo_group(self, user):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").send_keys(user.first_name)
        wd.find_element_by_name("middlename").send_keys(user.middle_name)
        wd.find_element_by_name("lastname").send_keys(user.last_name)
        wd.find_elements_by_css_selector("input[name=submit]")[0].click()
        self.app.return_to_home_page()

    def delete_by_name(self, first_name, last_name):
        wd = self.app.wd
        selector_text = "input[title='Select ({0} {1})']".format(first_name, last_name)
        wd.find_element_by_css_selector(selector_text).click()
        wd.find_element_by_css_selector("input[value=Delete]").click()
        wd.switch_to_alert().accept()
