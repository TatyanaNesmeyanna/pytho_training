from selenium import webdriver
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from fixture.session import SessionHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
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



    def destroy(self):
        self.wd.quit()
