from model.contact import Contact
import re

class ContactHelper:

    def __init__(self, app):
        self.app = app



    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.open_home_page()
        self.contact_cache = None

    def modify_first_contact(self, new_contact_data):
        self.modify_contact_by_index(0, new_contact_data)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # open modification form
        wd.find_elements_by_xpath("//img[ @ alt = 'Edit']")[index].click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.app.open_home_page()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()


    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("home", contact.home_phone)
        self.change_field_value("mobile", contact.mobile_phone)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("phone2", contact.secondary_phone)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        # select first contact
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[ @ value = 'Delete']").click()
        wd.switch_to_alert().accept()
        self.app.open_home_page()
        wd.find_element_by_css_selector("div.msgbox")
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self. contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            table_rows = wd.find_elements_by_tag_name("tr")
            for row in table_rows[1 : len(table_rows)]:
                cells = row.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text.splitlines()
                self. contact_cache.append(Contact(firstname = firstname, lastname = lastname, id = id, home_phone=all_phones[0],
                                                   mobile_phone=all_phones[1], work_phone=all_phones[2], secondary_phone=all_phones[3]))
        return list(self. contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute('value')
        lastname = wd.find_element_by_name("lastname").get_attribute('value')
        id = wd.find_element_by_name("id").get_attribute('value')
        home_phone = wd.find_element_by_name("home").get_attribute('value')
        mobile_phone = wd.find_element_by_name("mobile").get_attribute('value')
        work_phone = wd.find_element_by_name("work").get_attribute('value')
        secondary_phone = wd.find_element_by_name("phone2").get_attribute('value')
        return(Contact(firstname=firstname, lastname=lastname, home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone, secondary_phone=secondary_phone, id=id))

    def contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        secondary_phone = re.search("P: (.*)", text).group(1)
        return(Contact(home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone, secondary_phone=secondary_phone, id=id))





