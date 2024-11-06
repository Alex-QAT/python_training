# -*- coding: utf-8 -*-

from fixture.application import Application
from model.group import Group

import pytest


def test_add_group(app):
        #app.session.login("admin", "secret")
        app.group.create(Group("new_group_firefox", "jhklpjhlksdjal;fkj", "полфкджплкпмдкфж"))
        #app.session.logout()

def test_add_emptygroup(app):
        app.group.create(Group("", "", ""))



