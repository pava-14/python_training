from selenium import webdriver

from fixture.group import GroupHelper
from fixture.session import SessionHelper
from fixture.user import UserHelper
from util.util import get_random_string


class Application:
    def __init__(self, browser, base_url):
        if browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError(f"Unrecognized browser {browser}")
        # self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.user = UserHelper(self)
        self.base_url = base_url

        # self.start_page_url = "http://localhost/addressbook/index.php"
        self.user_name = "admin"
        self.user_pass = "secret"
        #
        # postfix = get_random_string()
        # self.group_name = "Group_" + postfix
        # self.group_header = "Header_" + postfix
        # self.group_footer = "Footer_" + postfix
        # self.first_name = "Bob_" + postfix
        # self.middle_name = "N_" + postfix
        # self.last_name = "Marley_" + postfix

    def is_valid(self):
        try:
            self.wd.current_url()
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements_by_id("search_count")) > 0):
            wd.get(self.base_url)

    def return_to_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    def destroy(self):
        self.wd.quit()
