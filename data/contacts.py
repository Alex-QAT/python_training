from model.contact import Contact
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation
    return prefix + "".join([random.choice(symbols)
                             for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", midlename="", lastname="", nickname="", tittle="", company="", address="", home="", mobile="", work="", fax="", email="", email2="", email3="", homepage="", bday="", bmonth="-", byear="", aday="", amonth="-", ayear="",)] + [Contact(firstname=random_string("=firstname=", 10), midlename=random_string("=midlename=", 10), lastname=random_string("=lastname=", 10), nickname=random_string("=nickname=", 10), tittle=random_string("=tittle=", 10), company=random_string("=company=", 10), address=random_string("=address=", 10), home=random_string("=home=", 10), mobile=random_string("=mobile=", 10), work=random_string("=work=", 10), fax=random_string("=fax=", 10), email=random_string("=email=", 10), email2=random_string("=email2=", 10), email3=random_string("=email3=", 10), homepage=random_string("=homepage=", 10), bday="", bmonth="-", byear="", aday="", amonth="-", ayear="",)
                                                     for i in range(5)]