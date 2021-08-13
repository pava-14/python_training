from selenium import webdriver

from fixture.group import GroupHelper
from fixture.session import SessionHelper
from fixture.user import UserHelper


class Application:
    # def __init__(self, browser, base_url, username, password):
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
        # self.user_name = username
        # self.user_pass = password

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
