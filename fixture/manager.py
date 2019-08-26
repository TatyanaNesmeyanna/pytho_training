from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from fixture.session import SessionHelper


class HelpersManager:
    def __init__(self, app):
        self.app = app

    def init_helpers(self):
        self.app.group = GroupHelper(self.app)
        self.app.contact = ContactHelper(self.app)
        self.app.session = SessionHelper(self.app)
