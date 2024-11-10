# -*- coding: utf-8 -*-

from fixture.application import Application
from model.contact import Contact

import pytest



def test_add_contact(app):
    # получаем список контактов
    old_con = app.contact.get_con_list()
    # кладём в переменную объект контакта который будем добавлять
    con = Contact(u"Иван", u"Васильевич", u"Сергеев", "John",
                             u"Начальник департамента проектных решений", u"Лукойл", u"Москва, Чистые пруды 19",
                             "+7-495-256-08-53", "+7-988-556-33-11", "+7-987-556-44-22", "3-33-43", "jonnydep@mail.ru",
                             "jonnydep2@mail.ru", "jonnydep3@mail.ru", "www.vk.com/ciberded", "27", "October", "1984",
                             "15", "November", "2024")
    # метод добавления контакта, с использованием  вышеуказанной переменной в параметре
    app.contact.add_new(con)
    # получаем новый список контактов
    new_con = app.contact.get_con_list()
    # сравниваем списки контактов по количеству (новый на 1 больше старого)
    assert len(old_con) + 1 == len(new_con)
    # добавляем в старый список тот же самый контакт из переменной
    old_con.append(con)
    # сравниваем отсортированные по ID списки контактов (должны быть идентичны друг другу)
    assert sorted(old_con, key=Contact.id_or_max) == sorted(new_con, key=Contact.id_or_max)



def test_add_contact_new(app):
    old_con = app.contact.get_con_list()
    con = Contact(u"", u"", u"", "",
                             u"", u"", u"", "",
                             "", "", "", "", "",
                             "", "", "20", "October", "1990", "15",
                             "November", "2024")
    app.contact.add_new(con)
    new_con = app.contact.get_con_list()
    assert len(old_con) + 1 == len(new_con)
    old_con.append(con)
    assert sorted(old_con, key=Contact.id_or_max) == sorted(new_con, key=Contact.id_or_max)

