# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(first_name="FirstName", middlename="Middlename", lastname="Lastname", nickname="Nickname", title="Title", company="Company", address="Address", home="1",
                               mobile_phone="777777", work_phone="666666", fax="555555", email="test@mail.ru", address2="test adress", phone2="1", notes="no"))


def test_add_empty_contact(app):
    app.contact.create(Contact(first_name="", middlename="", lastname="", nickname="", title="", company="", address="", home="",
                             mobile_phone="", work_phone="", fax="", email="", address2="", phone2="", notes=""))

