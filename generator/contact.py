from model.contact import Contact
import random
import string
import os.path
import json
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n=int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_phone_number():
    n_groups = random.randint(3, 6)
    symbols = string.digits + "-"
    return ('-'.join([''.join(random.choices(symbols, k=random.randint(1, 3))) for _ in range(n_groups)]))

testdata=[Contact(firstname="", lastname="", home_phone="",
                               mobile_phone="", work_phone="", secondary_phone="")] + [Contact(firstname=random_string("FirstName", 10), lastname=random_string("LastName", 10), home_phone=random_phone_number(),
                               mobile_phone=random_phone_number(), work_phone=random_phone_number(), secondary_phone=random_phone_number()) for i in range(n)]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, "w") as out:
    out.write(json.dumps(testdata, default= lambda  x: x.__dict__, indent=2))
