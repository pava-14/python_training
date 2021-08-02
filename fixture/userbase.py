from selenium import webdriver
from selenium.webdriver.common.by import By


class UserPageBase:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(60)
        self.start_page_url = "http://localhost/addressbook/index.php"
        self.user_name = "admin"
        self.user_pass = "secret"
        self.first_name = "Bob"
        self.middle_name = "N"
        self.last_name = "Marley"

    def destroy(self):
        self.wd.quit()

    def logout(self):
        self.wd.find_element(By.LINK_TEXT, "Logout").click()

    def return_to_home_page(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "home page").click()

    def open_home_page(self):
        wd = self.wd
        wd.get(self.start_page_url)

    def login(self, user_name, user_pass):
        wd = self.wd
        self.open_home_page()
        wd.find_element(By.NAME, "user").send_keys(user_name)
        wd.find_element(By.NAME, "pass").send_keys(user_pass)
        wd.find_element(By.CSS_SELECTOR, "input[type=submit]").click()

    def add_new_user_wo_group(self, user):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "add new").click()
        wd.find_element(By.NAME, "firstname").send_keys(user.first_name)
        wd.find_element(By.NAME, "middlename").send_keys(user.middle_name)
        wd.find_element(By.NAME, "lastname").send_keys(user.last_name)
        self.wd.find_elements(By.CSS_SELECTOR, "input[name=submit]")[0].click()
        self.return_to_home_page()
