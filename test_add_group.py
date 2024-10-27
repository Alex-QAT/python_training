# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

from application import Application
from group import Group

import pytest

@pytest.fixture

def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):

        app.login("admin", "secret")
        app.create_group(Group("new_group_firefox", "jhklpjhlksdjal;fkj", "полфкджплкпмдкфж"))
        app.logout()

def test_add_emptygroup(app):

        app.login("admin", "secret")
        app.create_group(Group("", "", ""))
        app.logout()


