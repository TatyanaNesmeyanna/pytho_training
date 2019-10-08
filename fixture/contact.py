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

    def modify_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        # open modification form
        table_rows = wd.find_elements_by_tag_name("tr")
        input_el = wd.find_element_by_css_selector("input[value='%s']" % id)
        cell = input_el.find_element_by_xpath('..')
        row = cell.find_element_by_xpath('..')
        edit_index = table_rows.index(row)-1
        wd.find_elements_by_xpath("//img[ @ alt = 'Edit']")[edit_index].click()
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

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()


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

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        # select first contact
        self.select_contact_by_id(id)
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
                all_phones = cells[5].text
                address = cells[3].text
                all_emails = cells[4].text
                self. contact_cache.append(Contact(firstname = firstname, lastname = lastname, address = address, all_emails_from_home_page = all_emails, id = id, all_phones_from_home_page= all_phones))
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
        email1 = wd.find_element_by_name("email").get_attribute('value')
        email2 = wd.find_element_by_name("email2").get_attribute('value')
        email3 = wd.find_element_by_name("email3").get_attribute('value')
        address = wd.find_element_by_name("address").text
        return(Contact(firstname=firstname, lastname=lastname, home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone, secondary_phone=secondary_phone, address=address, email1=email1, email2=email2, email3=email3, id=id))

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone= re.search("H: (.*)", text).group(1) if re.search("H: (.*)", text) else ""
        work_phone = re.search("W: (.*)", text).group(1) if re.search("W: (.*)", text) else ""
        mobile_phone = re.search("M: (.*)", text).group(1) if re.search("M: (.*)", text) else ""
        secondary_phone = re.search("P: (.*)", text).group(1) if re.search("P: (.*)", text) else ""
        return(Contact(home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone, secondary_phone=secondary_phone, id=id))

    def add_contact_to_group(self, contact, group):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_id(contact.id).click()
        wd.find_element_by_name("to_group").click()
        wd.find_element_by_xpath('//select[@name="to_group"]//option[@ value="%s"]' % group.id ).click()
        wd.find_element_by_name("to_group").click()
        wd.find_element_by_name("add").click()
        wd.find_element_by_link_text("group page \""+group.name+"\"").click()





