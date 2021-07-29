# ~*~ coding: utf-8 ~*~

from selenium import webdriver
from selenium.webdriver.common.by import By

from user import User


class TestAddNewUser:
    def setup_method(self):
        self.driver = webdriver.Firefox()
        self.vars = {}
        self.url = "http://localhost/addressbook/index.php"
        self.user_name = "admin"
        self.user_pass = "secret"
        self.first_name = "Bob"
        self.middle_name = "N"
        self.last_name = "Marley"

    def teardown_method(self):
        self.driver.quit()

    def open_home_page(self, wd, url):
        wd.get(url)

    def logout(self, wd):
        wd.find_element(By.LINK_TEXT, "Logout").click()
        # elm = wd.find_element(By.LINK_TEXT, "Logout")
        # elm.click()

    def login(self, wd, user_name, user_pass):
        wd.find_element(By.NAME, "user").send_keys(user_name)
        wd.find_element(By.NAME, "pass").send_keys(user_pass)
        wd.find_element(By.CSS_SELECTOR, "input[type=submit]").click()

    def return_to_home_page(self, wd):
        wd.find_element(By.LINK_TEXT, "home page").click()

    def add_new_user_wo_group(self, wd, user):
        wd.find_element(By.LINK_TEXT, "add new").click()
        wd.find_element(By.NAME, "firstname").send_keys(user.first_name)
        wd.find_element(By.NAME, "middlename").send_keys(user.middle_name)
        wd.find_element(By.NAME, "lastname").send_keys(user.last_name)
        self.driver.find_elements(By.CSS_SELECTOR, "input[name=submit]")[0].click()

    def test_add_new_user_wo_group(self):
        wd = self.driver
        self.open_home_page(wd, self.url)
        self.login(wd, user_name=self.user_name, user_pass=self.user_pass)
        self.add_new_user_wo_group(wd, User(first_name=self.first_name, middle_name=self.middle_name,
                                            last_name=self.last_name))
        self.return_to_home_page(wd)
        self.logout(wd)
