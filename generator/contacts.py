from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f", ["number of groups", "file"])
except getopt.GetoptError as err:
    # print help information and exit:
    print(err)  # will print something like "option -a not recognized"
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
        if o == "-n":
            n = int(a)
        elif o == "-f":
            f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation
    return prefix + "".join([random.choice(symbols)
                             for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", midlename="", lastname="", nickname="", tittle="", company="", address="", home="", mobile="", work="", fax="", email="", email2="", email3="", homepage="", bday="", bmonth="-", byear="", aday="", amonth="-", ayear="",)] + [Contact(firstname=random_string("=firstname=", 10), midlename=random_string("=midlename=", 10), lastname=random_string("=lastname=", 10), nickname=random_string("=nickname=", 10), tittle=random_string("=tittle=", 10), company=random_string("=company=", 10), address=random_string("=address=", 10), home=random_string("=home=", 10), mobile=random_string("=mobile=", 10), work=random_string("=work=", 10), fax=random_string("=fax=", 10), email=random_string("=email=", 10), email2=random_string("=email2=", 10), email3=random_string("=email3=", 10), homepage=random_string("=homepage=", 10), bday="", bmonth="-", byear="", aday="", amonth="-", ayear="",)
                                                     for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as f_out:
    jsonpickle.set_encoder_options("json", indent=2)
    f_out.write(jsonpickle.encode(testdata))