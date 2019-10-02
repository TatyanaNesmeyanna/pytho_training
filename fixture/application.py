from selenium import webdriver
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from fixture.session import SessionHelper
from selenium.common.exceptions import NoSuchElementException


class Application:
    def __init__(self, browser, base_url):
        if browser=="firefox":
            self.wd = webdriver.Firefox()
        elif browser=="Chrome":
            self.wd = webdriver.Chrome()
        elif browser=="ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(1)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.session = SessionHelper(self)
        self.base_url = base_url

    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url.endswith("/addressbook/")):
            wd.get(self.base_url)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def is_login_page(self):
        try:
            self.wd.find_element_by_name("pass")
            return True
        except NoSuchElementException:
            return False

    def destroy(self):
        self.wd.quit()
