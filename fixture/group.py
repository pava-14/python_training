from selenium.webdriver.common.by import By


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "groups").click()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "group page").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element(By.NAME, "new").click()
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        wd.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()

    def delete_first(self):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element(By.NAME, "selected[]").click()
        wd.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()

    def delete_by_name(self, group_name):
        wd = self.app.wd
        self.open_groups_page()
        selector_text = "input[title='Select ({0})']".format(group_name)
        wd.find_element_by_css_selector(selector_text).click()
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def edit_by_name(self, group_name):
        wd = self.app.wd
        self.open_groups_page()
        selector_text = "input[title='Select ({0})']".format(group_name)
        wd.find_element_by_css_selector(selector_text).click()
        wd.find_element_by_name("edit").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("{0}_edited".format(group_name))
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
