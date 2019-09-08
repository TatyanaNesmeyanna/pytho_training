class Contact:
    def __init__(self, first_name=None, middlename=None, lastname=None, nickname=None, title=None, company=None, address=None, home=None,
                       mobile_phone=None, work_phone=None, fax=None, email=None, address2=None, phone2=None, notes=None, id=None):
        self.first_name = first_name
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.email = email
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id= id

    def __repr__(self):
        return "%s:%s:%s" % (self.first_name, self.lastname, self.name)

    def __eq__(self, other):
        return ((self.id == other.id) and (self.first_name == other.first_name) and (self.lastname == other.lastname))
