# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string

constant = [
    Contact(firstname="firstname1", lastname="lastname1", home_phone="111", mobile_phone="222", work_phone="333", secondary_phone="444"),
    Contact(firstname="firstname2", lastname="lastname2", home_phone="101", mobile_phone="202", work_phone="303", secondary_phone="404"),
]

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_phone_number():
    n_groups = random.randint(3, 6)
    symbols = string.digits + "-"
    return ('-'.join([''.join(random.choices(symbols, k=random.randint(1, 3))) for _ in range(n_groups)]))

testdata=[Contact(firstname="", lastname="", home_phone="",
                               mobile_phone="", work_phone="", secondary_phone="")] + [Contact(firstname=random_string("FirstName", 10), lastname=random_string("LastName", 10), home_phone=random_phone_number(),
                               mobile_phone=random_phone_number(), work_phone=random_phone_number(), secondary_phone=random_phone_number()) for i in range(5)]
