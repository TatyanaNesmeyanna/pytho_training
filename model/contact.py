from sys import maxsize

class Contact:
    def __init__(self, firstname=None, lastname=None, home_phone=None,
                       mobile_phone=None, work_phone=None,  secondary_phone=None, id=None, all_phones_from_home_page = None, address = None,
                            all_emails_from_home_page = None, email1=None, email2=None, email3=None):
        self.firstname = firstname
        self.lastname = lastname
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.secondary_phone = secondary_phone
        self.id = id
        self.all_phones_from_home_page =all_phones_from_home_page
        self.address = address
        self.all_emails_from_home_page = all_emails_from_home_page
        self.email1=email1
        self.email2 = email2
        self.email3 = email3


    def __repr__(self):
        return "%s:%s:%s;%s;%s;%s;%s" % (self.firstname, self.lastname, self.id, self.home_phone, self.mobile_phone, self.work_phone,  self.secondary_phone)

    def __eq__(self, other):
        return ((self.id is None or other.id is None or self.id == other.id) and (self.firstname == other.firstname) and (self.lastname == other.lastname))

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
