# -*- coding: utf-8 -*-

from fixture.application import Application
from model.group import Group

import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation
    return prefix + "".join([random.choice(symbols)
                             for i in range(random.randrange(maxlen))])

testdata = [Group(name="", header="", footer="")] + [Group(name=random_string("=name=", 10), header=random_string("=header=", 20), footer=random_string("=footer=", 20))
                                                     for i in range(5)]
#
@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])


def test_add_group(app, group):
    # получаем список групп
    old_groups = app.group.get_gr_list()
    # переменная в которую положили группу, чтобы потом добавлять и в методе add и в старый список, для последующего сравнения списков
    #group = Group("new_group_firefox", "jhklpjhlksdjal;fkj", "полфкджплкпмдкфж")
    # метод добавления группы
    app.group.create(group)
    # сравниваем старый список групп и счётчик групп (старый на 1 меньше)
    assert len(old_groups) + 1 == app.group.count_gr()
    # получаем новый список
    new_groups = app.group.get_gr_list()
    #добавляем идентичную группу в старый список
    old_groups.append(group)
    # сравниваем отсортированные по ID списки групп (должны быть идентичны)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_add_emptygroup(app):
 #   old_groups = app.group.get_gr_list()
 #   group = Group("", "", "")
 #   app.group.create(group)
 #   new_groups = app.group.get_gr_list()
 #   assert len(old_groups) + 1 == len(new_groups)
 #   old_groups.append(group)
 #   assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

