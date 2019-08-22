# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.app.login(username="admin", password="secret")
    app.app.create_contact(Contact(first_name="FirstName", middlename="Middlename", lastname="Lastname", nickname="Nickname", title="Title", company="Company", address="Address", home="1",
                        mobile_phone="777777", work_phone="666666", fax="555555", email="test@mail.ru", adress2="test adress", phone2="1", notes="no"))
    app.app.logout()


def test_add_empty_contact(app):
    app.app.login(username="admin", password="secret")
    app.app.create_contact(Contact(first_name="", middlename="", lastname="", nickname="", title="", company="", address="", home="",
                        mobile_phone="", work_phone="", fax="", email="", adress2="", phone2="", notes=""))
    app.app.logout()

