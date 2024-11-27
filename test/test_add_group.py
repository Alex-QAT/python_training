# -*- coding: utf-8 -*-

from fixture.application import Application
from model.group import Group


#

def test_add_group(app, json_groups):
    group = json_groups
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

