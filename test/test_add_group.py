# -*- coding: utf-8 -*-

from fixture.application import Application
from model.group import Group

import pytest


def test_add_group(app):
    old_groups = app.group.get_gr_list()
    app.group.create(Group("new_group_firefox", "jhklpjhlksdjal;fkj", "полфкджплкпмдкфж"))
    new_groups = app.group.get_gr_list()
    assert len(old_groups) + 1 == len(new_groups)


def test_add_emptygroup(app):
    old_groups = app.group.get_gr_list()
    app.group.create(Group("", "", ""))
    new_groups = app.group.get_gr_list()
    assert len(old_groups) + 1 == len(new_groups)

