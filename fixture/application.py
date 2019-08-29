from selenium import webdriver
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from fixture.session import SessionHelper
from selenium.common.exceptions import NoSuchElementException


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(5)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.session = SessionHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

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
