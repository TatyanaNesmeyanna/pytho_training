# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(first_name="modified_name", middlename="", lastname="", nickname="", title="", company="", address="", home="",
                               mobile_phone="", work_phone="", fax="", email="", address2="", phone2="", notes=""))
    app.session.logout()


def test_modify_first_contact_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(first_name="second_modified_name"))
    app.session.logout()


def test_modify_first_contact_email(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(email="second_modified_email"))
    app.session.logout()
