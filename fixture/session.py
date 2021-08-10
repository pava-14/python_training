class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, user_name, user_pass):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("user").send_keys(user_name)
        wd.find_element_by_name("pass").send_keys(user_pass)
        wd.find_element_by_css_selector("input[type=submit]").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_elements_by_xpath("//div/div[1]/form/b").text[1:-1]

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
