# ~*~ coding: utf-8 ~*~

from selenium import webdriver
from selenium.webdriver.common.by import By

from group import Group


class TestGroupAdd:

    def setup_method(self):
        self.driver = webdriver.Firefox()
        self.vars = {}
        self.start_page_url = "http://localhost/addressbook/index.php"
        self.user_name = "admin"
        self.user_pass = "secret"
        self.group_name = "TestGroupSel"
        self.group_header = "TestGroupHeader"
        self.group_footer = "TestGroupFooter"

    def teardown_method(self):
        self.driver.quit()

    def open_home_page(self, wd):
        wd.get(self.start_page_url)

    def login(self, wd, user_name, user_pass):
        self.open_home_page(wd)
        # 4 | type | name=user | admin
        wd.find_element(By.NAME, "user").send_keys(user_name)
        # 5 | type | name=pass | secret
        wd.find_element(By.NAME, "pass").send_keys(user_pass)
        wd.find_element(By.CSS_SELECTOR, "input[type=submit]").click()

    def open_groups_page(self, wd):
        wd.find_element(By.LINK_TEXT, "groups").click()

    def create_group(self, wd, group):
        self.open_groups_page(wd)
        # 9 | type | name=group_name | TestGroupSel
        wd.find_element(By.NAME, "new").click()
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        # 10 | type | name=group_header | TestGroupHeader
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        # 11 | type | name=group_footer | TestGroupComment
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # 12 | click | name=submit |
        wd.find_element(By.NAME, "submit").click()
        self.return_to_groups_page(wd)

    def return_to_groups_page(self, wd):
        wd.find_element(By.LINK_TEXT, "groups").click()

    def logout(self, wd):
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def test_group_add(self):
        # Test name: TestGroupAddSel
        # Step # | name | target | value
        wd = self.driver
        self.login(wd, user_name=self.user_name, user_pass=self.user_pass)
        self.create_group(wd, Group(name=self.group_name, header=self.group_header,
                                    footer=self.group_footer))
        # TODO: Check for group_name
        # do something
        #
        self.logout(wd)

    def test_empty_group_add(self):
        # Test name: TestGroupAddSel
        # Step # | name | target | value
        wd = self.driver
        self.login(wd, user_name=self.user_name, user_pass=self.user_pass)
        self.create_group(wd, Group(name="", header="", footer=""))
        # TODO: Check for group_name
        # do something
        #
        self.logout(wd)
