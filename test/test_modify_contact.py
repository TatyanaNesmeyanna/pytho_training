# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_modify_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test_delete_contact"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    modified_contact = Contact(firstname="modified_name"+'_'+str(contact.id))
    modified_contact.id = contact.id
    modified_contact.lastname = contact.lastname
    app.contact.modify_contact_by_id(modified_contact.id, modified_contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts_with_modified_contact = [modified_contact if modified_contact.id == el.id else el for el in old_contacts]
    assert sorted(old_contacts_with_modified_contact, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key = Contact.id_or_max) == sorted(app.contact.get_contact_list(), key = Contact.id_or_max)

# def test_modify_contact_name(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname = "test_modify_contact"))
#     old_contacts = app.contact.get_contact_list()
#     index = randrange(len(old_contacts))
#     contact = Contact(firstname="modified_name"+'_'+str(index))
#     contact.id = old_contacts[index].id
#     contact.lastname = old_contacts[index].lastname
#     app.contact.modify_contact_by_index(index, contact)
#     assert len(old_contacts) == app.contact.count()
#     new_contacts = app.contact.get_contact_list()
#     old_contacts[index] = contact
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



