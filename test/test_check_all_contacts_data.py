# -*- coding: utf-8 -*-
from fixture.orm import ORMFixture
from model.contact import Contact
import re
import allure


def test_check_all_contacts_data(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="firstname", lastname="lastname", address="address",
                                    home_phone="123", work_phone="456", mobile_phone="789", secondary_phone="135",
                                        email1="1@gmail.com", email2="2@gmail.com", email3="3@gmail.com"))
    with allure.step('Given contact list from db and from homepage'):
        contacts_from_homepage = sorted(app.contact.get_contact_list(),key=Contact.id_or_max)
        db = ORMFixture(host = "127.0.0.1", name = "addressbook", user = "root", password = "")
        contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    with allure.step('When I get contact email and phones from db and homepage'):
        for c in contacts_from_db:
            c.all_phones_from_home_page = merge_phones_like_on_home_page(c)
            c.all_emails_from_home_page = merge_emails_like_on_home_page(c)
        list_of_phones_from_db=[]
        list_of_emails_from_db=[]
        list_of_phones_from_home_page = []
        list_of_emails_from_home_page = []
        for i in range(0, len(contacts_from_db)):
            list_of_phones_from_db.append(contacts_from_db[i].all_phones_from_home_page)
            list_of_emails_from_db.append(contacts_from_db[i].all_emails_from_home_page)
            list_of_phones_from_home_page.append(contacts_from_homepage[i].all_phones_from_home_page)
            list_of_emails_from_home_page.append(contacts_from_homepage[i].all_emails_from_home_page)
    with allure.step('Then contact data from db should be equal to contact data from home page'):
        assert contacts_from_db == contacts_from_homepage
        assert list_of_phones_from_db == list_of_phones_from_home_page
        assert list_of_emails_from_db == list_of_emails_from_home_page

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x : x!="",
                            map(lambda x : clear(x),
                                filter(lambda x : x is not None,
                                       [contact.home_phone, contact.mobile_phone, contact.work_phone, contact.secondary_phone]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                       [contact.email1, contact.email2, contact.email3])))