from selenium import webdriver

from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.session import SessionHelper
from selenium.webdriver.chrome.options import Options


class Application:
    def __init__(self, browser, base_url):
        if browser == "chrome":
            options = Options()
            # Runs Chrome in headless mode.
            options.add_argument("--headless")
            # Bypass OS security model
            options.add_argument('--no-sandbox')
            # applicable to windows os only
            # options.add_argument('--disable-gpu')
            options.add_argument('start-maximized')  #
            options.add_argument('disable-infobars')
            options.add_argument("--disable-extensions")
            self.wd = webdriver.Chrome(options=options)
            # self.wd = webdriver.Chrome(chrome_options=options)
            # driver = webdriver.Chrome(chrome_options=options,
            #                           executable_path=r'C:\path\to\chromedriver.exe')
        elif browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError(f"Unrecognized browser {browser}")
        # self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url()
            return True
        except Exception:
            print(Exception)
            return False

    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url.endswith("/index.php")
                and len(wd.find_elements_by_id("search_count")) > 0):
            wd.get(self.base_url)

    def return_to_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    def destroy(self):
        self.wd.quit()
