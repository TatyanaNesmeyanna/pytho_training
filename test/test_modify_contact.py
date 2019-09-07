# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name = "test_delete_contact"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(first_name="modified_name", middlename="", lastname="", nickname="", title="", company="", address="", home="",
                               mobile_phone="", work_phone="", fax="", email="", address2="", phone2="", notes=""))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_modify_first_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name = "test_delete_contact"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(first_name="second_modified_name"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_first_contact_email(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name = "test_delete_contact"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(email="second_modified_email"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
