from model.contact import Contact
from model.group import Group
from random import randrange

def test_con_add_to_gr(app, orm):
    # предусловие на наличие контактов (если нет - создаём)
    if app.contact.count_con() == 0:
        app.contact.add_new(Contact(firstname="Петя"))
    # проверка предусловия (если группы отсутствуют - то создать группу, иначе ничего не делать)
    if app.group.count_gr() == 0:
        app.group.create(Group("test-group"))

    # получаем список групп из БД
    l_gr = orm.get_gr_list()
    # получаем индекс случайной группы
    gr_id = randrange(len(l_gr))
    # получаем случайную группу
    group = l_gr[gr_id]

    # получаем список контактов из БД не входящих в выбранную группу
    l_con = orm.get_con_not_in_gr(group)
    # если список пуст, то добавляем новый контакт и вновь берём такой же список контактов из БД (теперь там точно есть такой контакт)
    if l_con == []:
        app.contact.add_new(Contact(firstname="Федя"))
        l_con = orm.get_con_not_in_gr(group)

    # получаем индекс случаного контакта из выбранного списка
    con_id = randrange(len(l_con))
    # получаем случайный контакт из выбранного списка
    contact = l_con[con_id]

    # получаем список контактов в группе после удаления (для постпроверки)
    cons_in_gr_bef = orm.get_con_in_gr(group)
    # добавление контакта в группу, где параметрами передаются contact.id - идентификатор случ. контакта, а group.id - идентификатор случайной группы
    app.contact.con_add_to_gr(contact.id, group.id)

    # отладочный вывод контакта
    print("\nID контакта: ", contact.id)
    # отладочный вывод группы
    print("ID группы: ", group.id)

    # постпроверка: сравнить список контактов входящих в группу до и после добавления
    #получаем список контактов в группе после операции добавления
    cons_in_gr_aft = orm.get_con_in_gr(group)
    #к списку контактов до добавления прибавляем контакт который добавляли (тем самым выравнивая список до и после)
    cons_in_gr_bef.append(contact)
    # сама пост проверка: сортированный список "после" равен сортированному списку "до" + с прибавленным контактом, который добавляли в группу
    assert sorted(cons_in_gr_aft, key=Group.id_or_max) == sorted(cons_in_gr_bef, key=Group.id_or_max)






