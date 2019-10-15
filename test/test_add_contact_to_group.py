# -*- coding: utf-8 -*-
from fixture.orm import ORMFixture
from model.contact import Contact
from model.group import Group
import random
import pytest
import allure

def test_add_contact_to_group(app):
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    contact_for_test = None
    group_for_test = None
    if len(db.get_group_list()) == 0:
        group_for_test = Group(name="test_group")
        app.group.create(group_for_test)
        if len(db.get_contact_list()) == 0:
            contact_for_test = Contact(firstname = "test_contact")
            app.contact.create(contact_for_test)
        else:
            contact_for_test = random.choice(db.get_contact_list())
    else:
        if len(db.get_contact_list()) == 0:
            contact_for_test = Contact(firstname = "test_contact")
            app.contact.create(contact_for_test)
            group_for_test = random.choice(db.get_group_list())
        else:
            groups = db.get_group_list()
            contacts = db.get_contact_list()
            for c in contacts:
                if len(db.get_contacts_groups(c)) == len(groups):
                    continue
                else:
                    groups_without_contact= [g for g in groups if g not in db.get_contacts_groups(c)]
                    group_for_test = random.choice(groups_without_contact)
                    contact_for_test = c
                    break
    if contact_for_test is None:
         contact_for_test = Contact(firstname="test_contact")
         group_for_test = random.choice(db.get_group_list())
    with allure.step('Given contacts in groups list'):
        old_contact_list_in_group = db.get_contacts_in_group(group_for_test)
    with allure.step('When I add a contact %s to the gtoup %s' % (group_for_test , contact_for_test)):
        app.contact.add_contact_to_group(contact_for_test, group_for_test)
    with allure.step('Then the the contact %s  is in this group %s ' % (group_for_test ,contact_for_test)):
        new_contact_list_in_group = db.get_contacts_in_group(group_for_test)
        assert len(new_contact_list_in_group) == len(old_contact_list_in_group)+1
        old_contact_list_in_group.append(contact_for_test)
        assert sorted(old_contact_list_in_group, key = Contact.id_or_max) == sorted(new_contact_list_in_group, key = Contact.id_or_max)
