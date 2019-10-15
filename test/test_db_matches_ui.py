from model.group import Group
from model.contact import Contact
import allure

def test_group_list(app, db):
    with allure.step('Given a group list from UI'):
        ui_list = app.group.get_group_list()
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    with allure.step('When I get  a group list from DB'):
        db_list = map(clean, db.get_group_list())
    with allure.step('Then group list from UI should be equal to the group list from DB'):
        assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)

def test_contact_list(app, db):
    with allure.step('Given a contact list from UI'):
        ui_list = app.contact.get_contact_list()
    def clean(contact):
        return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip())
    with allure.step('When I get  a contact list from DB'):
        db_list = map(clean, db.get_contact_list())
    with allure.step('Then contact list from UI should be equal to the contact list from DB'):
        assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)



