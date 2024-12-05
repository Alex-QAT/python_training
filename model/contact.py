from sys import maxsize


class Contact:
    def __init__(self, firstname=None, midlename=None, lastname=None, nickname=None, tittle=None, company=None, address=None, home=None, mobile=None, work=None, fax=None, email=None, email2=None, email3=None, homepage=None, bday=None, bmonth=None, byear=None, aday=None, amonth=None, ayear=None, id=None, all_phones_hp=None, all_emails_hp=None):
        self.firstname = firstname
        self.midlename = midlename
        self.lastname = lastname
        self.nickname = nickname
        self.tittle = tittle
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.id = id
        self.all_phones_hp = all_phones_hp
        self.all_emails_hp = all_emails_hp

    # метод репрезентации
    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s:%s:%s:%s" % (self.id, self.lastname, self.firstname, self.home, self.mobile, self.work, self.email, self.email2, self.email3, self.address)

    # метод сравнения, задаём свои правила
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    # метод который возвращает либо id либо макс значение числа в python
    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
