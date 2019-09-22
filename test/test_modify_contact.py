# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name = "test_modify_contact"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="modified_name", middlename="", lastname="", nickname="", title="", company="", address="", home="",
                               mobile_phone="", work_phone="", fax="", email="", address2="", phone2="", notes="")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_modify_first_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name = "test_modify_contact"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="second_modified_name")
    contact.id = old_contacts[0].id
    contact.lastname = old_contacts[0].lastname
    app.contact.modify_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_first_contact_email(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name = "test_modify_contact"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(email="second_modified_email")
    contact.id = old_contacts[0].id
    contact.first_name = old_contacts[0].first_name
    contact.lastname = old_contacts[0].lastname
    app.contact.modify_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
