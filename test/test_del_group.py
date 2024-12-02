from random import randrange

from model.group import Group
import random



def test_del_rnd_gr(app, db): #c проверкой списков из БД и удалением по ID (из-за того, что способ сортировки в UI и в БД отличается)
    # предусловие если групп нет - то создаём, иначе ничего не делаем
    if len(db.get_gr_list()) == 0:
        app.group.create(Group("test-group", "бла бла бла", "ту ту ту"))
    # получаем старый список групп
    old_groups = db.get_gr_list()
    group = random.choice(old_groups)
    # метод удаления группы
    # app.group.del_1st_gr()
    app.group.del_gr_by_id(group.id)
    # сравниваем старый список и счётчик групп (старый список на 1 больше)
    assert len(old_groups) - 1 == app.group.count_gr()
    # получаем новый список
    new_groups = db.get_gr_list()
    #прибиваем в старом списке первую группу
    old_groups.remove(group)
    #сравниваем списки (должны быть идентичны)
    assert old_groups == new_groups

#def test_del_rnd_gr(app): #c проверкой списков из UI и удалением по индексу
#    # предусловие если групп нет - то создаём, иначе ничего не делаем
#    if app.group.count_gr() == 0:
#        app.group.create(Group("test-group", "бла бла бла", "ту ту ту"))
#    # получаем старый список групп
#    old_groups = app.group.get_gr_list()
#    #определяем индекс удаляемой группы
#    index = randrange(len(old_groups))
#    # метод удаления группы
#    # app.group.del_1st_gr()
#    app.group.del_gr_by_index(index)
#    # сравниваем старый список и счётчик групп (старый список на 1 больше)
#    assert len(old_groups) - 1 == app.group.count_gr()
#    # получаем новый список
#    new_groups = app.group.get_gr_list()
#    #прибиваем в старом списке первую группу
#    old_groups[index:index+1] = []
#    #сравниваем списки (должны быть идентичны)
#    assert old_groups == new_groups

#def test_del_1st_gr(app): # удаление первой группы в списке
#    # предусловие если групп нет - то создаём, иначе ничего не делаем
#    if app.group.count_gr() == 0:
#        app.group.create(Group("test-group", "бла бла бла", "ту ту ту"))
#    # получаем старый список групп
#    old_groups = app.group.get_gr_list()
#    # метод удаления группы
#    app.group.del_1st_gr()
#    # сравниваем старый список и счётчик групп (старый список на 1 больше)
#    assert len(old_groups) - 1 == app.group.count_gr()
#    # получаем новый список
#    new_groups = app.group.get_gr_list()
#    #прибиваем в старом списке первую группу
#    old_groups[0:1] = []
#    #сравниваем списки (должны быть идентичны)
#    assert old_groups == new_groups