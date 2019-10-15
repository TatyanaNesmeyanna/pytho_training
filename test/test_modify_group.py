# -*- coding: utf-8 -*-
from model.group import Group
import random
import pytest
import allure

# def test_modify_first_group(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test"))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(name="modified_name", header="modified_header", footer="modified_footer"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)

def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    with allure.step('Given a group list'):
        old_groups = db.get_group_list()
    with allure.step('I select random group'):
        group = random.choice(old_groups)
        modified_group = Group(name="second_modified_name")
        modified_group.id = group.id
    with allure.step('When I modify a random group %s from the list' % modified_group):
        app.group.modify_group_by_id(group.id, modified_group)
    with allure.step('Then the new group list is equal to the old list with the modified group'):
        assert len(old_groups) == app.group.count()
        new_groups = db.get_group_list()
        old_groups_with_modified_group = [modified_group if modified_group.id==el.id else el for el in old_groups]
        assert sorted(old_groups_with_modified_group, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(new_groups, key = Group.id_or_max) == sorted(app.group.get_group_list(), key = Group.id_or_max)

