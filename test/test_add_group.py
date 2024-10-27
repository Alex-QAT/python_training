# -*- coding: utf-8 -*-

from fixture.application import Application
from model.group import Group

import pytest

@pytest.fixture

def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):

        app.session.login("admin", "secret")
        app.create_group(Group("new_group_firefox", "jhklpjhlksdjal;fkj", "полфкджплкпмдкфж"))
        app.session.logout()

def test_add_emptygroup(app):

        app.session.login("admin", "secret")
        app.create_group(Group("", "", ""))
        app.session.logout()


