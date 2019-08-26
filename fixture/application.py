from selenium import webdriver
from fixture.manager import HelpersManager


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.manager = HelpersManager(self)
        self.manager.init_helpers()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
