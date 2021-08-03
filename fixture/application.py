from selenium import webdriver
from selenium.webdriver.common.by import By

from fixture.group import GroupHelper
from fixture.session import SessionHelper
from fixture.user import UserHelper
from util.util import get_random_string


class Application:
    def __init__(self):
        # self.wd = webdriver.Firefox()
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(20)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.user = UserHelper(self)
        #
        self.start_page_url = "http://localhost/addressbook/index.php"
        self.user_name = "admin"
        self.user_pass = "secret"
        #
        postfix = get_random_string()
        self.group_name = "Group_" + postfix
        self.group_header = "Header_" + postfix
        self.group_footer = "Footer_" + postfix
        self.first_name = "Bob_" + postfix
        self.middle_name = "N_" + postfix
        self.last_name = "Marley_" + postfix

    def open_home_page(self):
        wd = self.wd
        wd.get(self.start_page_url)

    def return_to_home_page(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "home page").click()

    def destroy(self):
        self.wd.quit()
