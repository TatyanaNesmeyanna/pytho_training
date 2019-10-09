# -*- coding: utf-8 -*-
from fixture.orm import ORMFixture
from model.contact import Contact
from model.group import Group
import random

def test_delete_contact_from_group(app):
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    contact_for_test = None
    group_for_test = None
    if len(db.get_group_list()) == 0:
        group_for_test = Group(name="test_group")
        app.group.create(group_for_test)
        if len(db.get_contact_list()) == 0:
            contact_for_test = Contact(firstname = "test_contact")
            app.contact.create(contact_for_test)
            app.contact.add_contact_to_group(contact_for_test, group_for_test)
        else:
            contact_for_test = random.choice(db.get_contact_list())
            app.contact.add_contact_to_group(contact_for_test, group_for_test)
    else:
        if len(db.get_contact_list()) == 0:
            contact_for_test = Contact(firstname = "test_contact")
            app.contact.create(contact_for_test)
            group_for_test = random.choice(db.get_group_list())
            app.contact.add_contact_to_group(contact_for_test, group_for_test)
        else:
            contacts = db.get_contact_list()
            for c in contacts:
                if len(db.get_contacts_groups(c)) > 0:
                    contact_for_test=c
                    group_for_test = random.choice(db.get_contacts_groups(c))
                    break
    if contact_for_test is None:
         contact_for_test = random.choice(db.get_contact_list())
         group_for_test = random.choice(db.get_group_list())
         app.contact.add_contact_to_group(contact_for_test, group_for_test)
    old_contact_list_in_group = db.get_contacts_in_group(group_for_test)
    app.contact.delete_contact_from_group(contact_for_test, group_for_test)
    new_contact_list_in_group = db.get_contacts_in_group(group_for_test)
    assert len(new_contact_list_in_group) == len(old_contact_list_in_group)-1
    old_contact_list_in_group.remove(contact_for_test)
    assert sorted(old_contact_list_in_group, key = Contact.id_or_max) == sorted(new_contact_list_in_group, key = Contact.id_or_max)

