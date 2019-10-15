import re
import allure

def test_phones_on_home_page(app):
    with allure.step('Given a contact data from home page'):
        contact_from_home_page = app.contact.get_contact_list()[0]
    with allure.step('When I get the contact data from edit page'):
        contact_from_edit_page = app.contact.get_info_from_edit_page(0)
    with allure.step('Then contact phones from home page should be equal to the contact phones from edit page'):
        assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    with allure.step('Given a contact data from vieww page'):
        contact_from_view_page = app.contact.get_contact_from_view_page(0)
    with allure.step('When I get the contact data from edit page'):
        contact_from_edit_page = app.contact.get_info_from_edit_page(0)
    with allure.step('Then contact phones from view page should be equal to the contact phones from edit page'):
        assert contact_from_view_page.home_phone == contact_from_edit_page.home_phone
        assert contact_from_view_page.mobile_phone == contact_from_edit_page.mobile_phone
        assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone
        assert contact_from_view_page.secondary_phone == contact_from_edit_page.secondary_phone

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x : x!="",
                            map(lambda x : clear(x),
                                filter(lambda x : x is not None,
                                       [contact.home_phone, contact.mobile_phone, contact.work_phone, contact.secondary_phone]))))
