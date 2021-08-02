from selenium import webdriver
from selenium.webdriver.common.by import By

from fixture.group import GroupHelper
from fixture.session import SessionHelper
from fixture.user import UserHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(20)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.user = UserHelper(self)
        #
        self.start_page_url = "http://localhost/addressbook/index.php"
        self.user_name = "admin"
        self.user_pass = "secret"
        self.group_name = "TestGroupSel"
        self.group_header = "TestGroupHeader"
        self.group_footer = "TestGroupFooter"
        self.first_name = "Bob"
        self.middle_name = "N"
        self.last_name = "Marley"

    def open_home_page(self):
        wd = self.wd
        wd.get(self.start_page_url)

    def return_to_home_page(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "home page").click()

    def destroy(self):
        self.wd.quit()
