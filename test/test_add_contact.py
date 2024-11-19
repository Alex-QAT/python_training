# -*- coding: utf-8 -*-

from fixture.application import Application
from model.contact import Contact

import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation
    return prefix + "".join([random.choice(symbols)
                             for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", midlename="", lastname="", nickname="", tittle="", company="", address="", home="", mobile="", work="", fax="", email="", email2="", email3="", homepage="", bday="", bmonth="-", byear="", aday="", amonth="-", ayear="",)] + [Contact(firstname=random_string("=firstname=", 10), midlename=random_string("=midlename=", 10), lastname=random_string("=lastname=", 10), nickname=random_string("=nickname=", 10), tittle=random_string("=tittle=", 10), company=random_string("=company=", 10), address=random_string("=address=", 10), home=random_string("=home=", 10), mobile=random_string("=mobile=", 10), work=random_string("=work=", 10), fax=random_string("=fax=", 10), email=random_string("=email=", 10), email2=random_string("=email2=", 10), email3=random_string("=email3=", 10), homepage=random_string("=homepage=", 10), bday="", bmonth="-", byear="", aday="", amonth="-", ayear="",)
                                                     for i in range(5)]
#
@pytest.mark.parametrize("con", testdata, ids=[repr(x) for x in testdata])



def test_add_contact(app, con):
    # получаем список контактов
    old_con = app.contact.get_con_list()
    # кладём в переменную объект контакта который будем добавлять
    #con = Contact(u"Иван", u"Васильевич", u"Сергеев", "John",
    #                         u"Начальник департамента проектных решений", u"Лукойл", u"Москва, Чистые пруды 19",
    #                         "+7-495-256-08-53", "+7-988-556-33-11", "+7-987-556-44-22", "3-33-43", "jonnydep@mail.ru",
    #                         "jonnydep2@mail.ru", "jonnydep3@mail.ru", "www.vk.com/ciberded", "27", "October", "1984",
    #                         "15", "November", "2024")
    # метод добавления контакта, с использованием  вышеуказанной переменной в параметре
    app.contact.add_new(con)
    # сравниваем старый список и счётчик контактов по количеству (счётчик на 1 больше старого списка)
    assert len(old_con) + 1 == app.contact.count_con()
    # получаем новый список контактов
    new_con = app.contact.get_con_list()
    # добавляем в старый список тот же самый контакт из переменной
    old_con.append(con)
    # сравниваем отсортированные по ID списки контактов (должны быть идентичны друг другу)
    assert sorted(old_con, key=Contact.id_or_max) == sorted(new_con, key=Contact.id_or_max)

#@pytest.mark.parametrize("con", testdata, ids=[repr(x) for x in testdata])

#def test_add_contact_new(app, con):
#    old_con = app.contact.get_con_list()
    #con = Contact(u"", u"", u"", "",
#    #                         u"", u"", u"", "",
#    #                         "", "", "", "", "",
#    #                         "", "", "", "-", "", "",
#    #                         "-", "")
#    app.contact.add_new(con)
#    new_con = app.contact.get_con_list()
#    assert len(old_con) + 1 == len(new_con)
#    old_con.append(con)
#    assert sorted(old_con, key=Contact.id_or_max) == sorted(new_con, key=Contact.id_or_max)

