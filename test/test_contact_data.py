from model.contact import Contact
from random import randrange
import re


def test_contact_data_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="firstname", lastname="lastname", address="address",
                                    home_phone="123", work_phone="456", mobile_phone="789", secondary_phone="135",
                                        email1="1@gmail.com", email2="2@gmail.com", email3="3@gmail.com"))
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_home_page = contacts[index]
    contact_from_edit_page = app.contact.get_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)

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