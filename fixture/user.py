from selenium.webdriver.common.by import By
from model.user import User


class UserHelper:
    def __init__(self, app):
        self.app = app

    def add_new_wo_group(self, user):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()
        wd.find_element(By.NAME, "firstname").send_keys(user.first_name)
        wd.find_element(By.NAME, "middlename").send_keys(user.middle_name)
        wd.find_element(By.NAME, "lastname").send_keys(user.last_name)
        wd.find_elements(By.CSS_SELECTOR, "input[name=submit]")[0].click()
        self.app.return_to_home_page()
