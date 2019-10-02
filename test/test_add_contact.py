# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_phone_number():
    n_groups = random.randint(3, 6)
    symbols = string.digits + "-"
    return ('-'.join([''.join(random.choices(symbols, k=random.randint(1, 3))) for _ in range(n_groups)]))

testdata=[Contact(firstname="", lastname="", home_phone="",
                               mobile_phone="", work_phone="", secondary_phone="")] + [Contact(firstname=random_string("FirstName", 10), lastname=random_string("LastName", 10), home_phone=random_phone_number(),
                               mobile_phone=random_phone_number(), work_phone=random_phone_number(), secondary_phone=random_phone_number()) for i in range(5)]

@pytest.mark.parametrize('contact', testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(contact)
    new_contacts = app.contact.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

