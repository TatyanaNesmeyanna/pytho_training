# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import pytest
from contact import Contact
from application import Application


class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_add_contact(self):
        self.app.login(username="admin", password="secret")
        self.app.create_contact(Contact(first_name="FirstName", middlename="Middlename", lastname="Lastname", nickname="Nickname", title="Title", company="Company", address="Address", home="1",
                            mobile_phone="777777", work_phone="666666", fax="555555", email="test@mail.ru", adress2="test adress", phone2="1", notes="no"))
        self.app.logout()

    def test_add_empty_contact(self):
        self.app.login(username="admin", password="secret")
        self.app.create_contact(Contact(first_name="", middlename="", lastname="", nickname="", title="", company="", address="", home="",
                            mobile_phone="", work_phone="", fax="", email="", adress2="", phone2="", notes=""))
        self.app.logout()
    
    def tearDown(self):
        self.app.destroy()


if __name__ == "__main__":
    unittest.main()
