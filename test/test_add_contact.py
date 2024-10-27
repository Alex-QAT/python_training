# -*- coding: utf-8 -*-

from fixture.application import Application
from model.contact import Contact

import pytest

@pytest.fixture

def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture



def test_add_contact(app):
    app.session.login("admin", "secret")
    app.add_new_contact(Contact(u"Иван", u"Васильевич", u"Сергеев", "John",
                             u"Начальник департамента проектных решений", u"Лукойл", u"Москва, Чистые пруды 19",
                             "+7-495-256-08-53", "+7-988-556-33-11", "+7-987-556-44-22", "3-33-43", "jonnydep@mail.ru",
                             "jonnydep2@mail.ru", "jonnydep3@mail.ru", "www.vk.com/ciberded", "27", "October", "1984",
                             "15", "November", "2024", "'October'", "29", "11"))
    app.session.logout()


def test_add_contact_new(app):
    app.session.login("admin", "secret")
    app.add_new_contact(Contact(u"", u"", u"", "",
                             u"", u"", u"", "",
                             "", "", "", "", "",
                             "", "", "20", "October", "1990", "15",
                             "November", "2024", "'October'", "29", "11"))
    app.session.logout()
