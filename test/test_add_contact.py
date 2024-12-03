# -*- coding: utf-8 -*-

from fixture.application import Application
from model.contact import Contact
import pytest
from data.contacts import testdata


#@pytest.mark.parametrize("con", testdata, ids=[repr(x) for x in testdata])

def test_add_contact(app, db, data_contacts, check_ui): # с проверкой данных по БД
    con = data_contacts
    # получаем список контактов
    old_con = db.get_con_list()
    # кладём в переменную объект контакта который будем добавлять
    #con = Contact(u"Иван", u"Васильевич", u"Сергеев", "John",
    #                         u"Начальник департамента проектных решений", u"Лукойл", u"Москва, Чистые пруды 19",
    #                         "+7-495-256-08-53", "+7-988-556-33-11", "+7-987-556-44-22", "3-33-43", "jonnydep@mail.ru",
    #                         "jonnydep2@mail.ru", "jonnydep3@mail.ru", "www.vk.com/ciberded", "27", "October", "1984",
    #                         "15", "November", "2024")
    # метод добавления контакта, с использованием  вышеуказанной переменной в параметре
    app.contact.add_new(con)
    # получаем новый список контактов
    new_con = db.get_con_list()
    # добавляем в старый список тот же самый контакт из переменной
    old_con.append(con)
    # сравниваем отсортированные по ID списки контактов (должны быть идентичны друг другу)
    assert sorted(old_con, key=Contact.id_or_max) == sorted(new_con, key=Contact.id_or_max)
    # отключаемая сверка списков, полученных из БД и из UI
    if check_ui:
        assert sorted(new_con, key=Contact.id_or_max) == sorted(app.contact.get_con_list(), key=Contact.id_or_max)

#def test_add_contact(app, data_contacts): # с проверками данных по UI
#    con = data_contacts
#    # получаем список контактов is UI
#    old_con = app.contact.get_con_list()
#    # кладём в переменную объект контакта который будем добавлять
#    #con = Contact(u"Иван", u"Васильевич", u"Сергеев", "John",
#    #                         u"Начальник департамента проектных решений", u"Лукойл", u"Москва, Чистые пруды 19",
#    #                         "+7-495-256-08-53", "+7-988-556-33-11", "+7-987-556-44-22", "3-33-43", "jonnydep@mail.ru",
#    #                         "jonnydep2@mail.ru", "jonnydep3@mail.ru", "www.vk.com/ciberded", "27", "October", "1984",
#    #                         "15", "November", "2024")
#    # метод добавления контакта, с использованием  вышеуказанной переменной в параметре
#    app.contact.add_new(con)
#    # сравниваем старый список и счётчик контактов по количеству (счётчик на 1 больше старого списка)
#    assert len(old_con) + 1 == app.contact.count_con()
#    # получаем новый список контактов
#    new_con = app.contact.get_con_list()
#    # добавляем в старый список тот же самый контакт из переменной
#    old_con.append(con)
#    # сравниваем отсортированные по ID списки контактов (должны быть идентичны друг другу)
#    assert sorted(old_con, key=Contact.id_or_max) == sorted(new_con, key=Contact.id_or_max)

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

