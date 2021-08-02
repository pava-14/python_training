from selenium import webdriver
from selenium.webdriver.common.by import By
from fixture.session_group import SessionHelperGroup


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(60)
        self.session = SessionHelperGroup(self)
        #
        self.start_page_url = "http://localhost/addressbook/index.php"
        self.user_name = "admin"
        self.user_pass = "secret"
        self.group_name = "TestGroupSel"
        self.group_header = "TestGroupHeader"
        self.group_footer = "TestGroupFooter"

    def open_home_page(self):
        wd = self.wd
        wd.get(self.start_page_url)

    def open_groups_page(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "groups").click()

    def create_group(self, group):
        wd = self.wd
        self.open_groups_page()
        wd.find_element(By.NAME, "new").click()
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        wd.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "groups").click()

    def destroy(self):
        self.wd.quit()
