from random import randrange

from model.contact import Contact

def test_edit_rnd_con_by_id(app, db): # списки контактов получаем из БД
    # преусловие на наличие контактов (если нет - создаём)
    if app.contact.count_con() == 0:
        app.contact.add_new(Contact(firstname="Петя"))
    # получаем список контактов из БД
    old_con = db.get_con_list()
    index = randrange(len(old_con))
    # переменная с контактом чтоб добавить одно и то же и в методе и в старый список для последующего сравнения
    con = Contact(u"Вася", u"Иванович", u"Васильев", "Peter",
                             u"Начальник отдела продаж", u"Grass", u"Волгоград, Аллея героев 23",
                             "+7-495-536-18-27", "+7-917-568-44-45", "+7-988-332-11-25", "4-05-18", "peterpen@mail.ru",
                             "peterpen2@mail.ru", "peterpen3@mail.ru", "www.vk.com/peter_1st", "12", "September", "1981",
                             "12", "January", "2025")
    # запомнили id первого по списку контакта из старого списка
    con.id = old_con[index].id
    # метод редактирования контакта
    app.contact.edit_by_id(con.id, con)
    # сравниваем старый и счётчик контактов по количеству контактов (должны быть равны)
    assert len(old_con) == app.contact.count_con()
    # получаем новый список контактов из БД
    new_con = db.get_con_list()
    old_con[index] = con
    assert sorted(old_con, key=Contact.id_or_max) == sorted(new_con, key=Contact.id_or_max)

#def test_edit_rnd_con_by_index(app): # списки контактов получаем из UI
#    # преусловие на наличие контактов (если нет - создаём)
#    if app.contact.count_con() == 0:
#        app.contact.add_new(Contact(firstname="Петя"))
#    # получаем список контактов из UI
#    old_con = app.contact.get_con_list()
#    index = randrange(len(old_con))
#    # переменная с контактом чтоб добавить одно и то же и в методе и в старый список для последующего сравнения
#    con = Contact(u"Вася", u"Иванович", u"Васильев", "Peter",
#                             u"Начальник отдела продаж", u"Grass", u"Волгоград, Аллея героев 23",
#                             "+7-495-536-18-27", "+7-917-568-44-45", "+7-988-332-11-25", "4-05-18", "peterpen@mail.ru",
#                             "peterpen2@mail.ru", "peterpen3@mail.ru", "www.vk.com/peter_1st", "12", "September", "1981",
#                             "12", "January", "2025")
#    # запомнили id первого по списку контакта из старого списка
#    con.id = old_con[index].id
#    # метод редактирования контакта
#    app.contact.edit_by_index(index, con)
#    # сравниваем старый и счётчик контактов по количеству контактов (должны быть равны)
#    assert len(old_con) == app.contact.count_con()
#    # получаем новый список контактов из UI
#    new_con = app.contact.get_con_list()
#    old_con[index] = con
#    assert sorted(old_con, key=Contact.id_or_max) == sorted(new_con, key=Contact.id_or_max)

#def test_edit_1st_con(app):
#    # преусловие на наличие контактов (если нет - создаём)
#    if app.contact.count_con() == 0:
#        app.contact.add_new(Contact(firstname="Петя"))
#    # получаем список контактов
#    old_con = app.contact.get_con_list()
#    # переменная с контактом чтоб добавить одно и то же и в методе и в старый список для последующего сравнения
#    con = Contact(u"Вася", u"Иванович", u"Васильев", "Peter",
#                             u"Начальник отдела продаж", u"Grass", u"Волгоград, Аллея героев 23",
#                             "+7-495-536-18-27", "+7-917-568-44-45", "+7-988-332-11-25", "4-05-18", "peterpen@mail.ru",
#                             "peterpen2@mail.ru", "peterpen3@mail.ru", "www.vk.com/peter_1st", "12", "September", "1981",
#                             "12", "January", "2025")
#    # запомнили id первого по списку контакта из старого списка
#    con.id = old_con[0].id
#    # метод редактирования контакта
#    app.contact.edit_1st(con)
#    # сравниваем старый и счётчик контактов по количеству контактов (должны быть равны)
#    assert len(old_con) == app.contact.count_con()
#    # получаем новый список контакта
#    new_con = app.contact.get_con_list()
#    old_con[0] = con
#    assert sorted(old_con, key=Contact.id_or_max) == sorted(new_con, key=Contact.id_or_max)

#def test_edit_1st_con_firstname(app):
#    if app.contact.count_con() == 0:
#        app.contact.add_new(Contact(firstname="Петя"))
#    old_con = app.contact.get_con_list()
#    con = Contact(firstname="Сергей")
#    con.id = old_con[0].id
#    con.firstname = old_con[0].firstname
#    con.lastname = old_con[0].lastname
#    app.contact.edit_1st(con)
#    new_con = app.contact.get_con_list()
#    assert len(old_con) == len(new_con)
#    old_con[0] = con
#    assert sorted(old_con, key=Contact.id_or_max) == sorted(new_con, key=Contact.id_or_max)

#def test_edit_1st_con_mdlname(app):
#    if app.contact.count_con() == 0:
#        app.contact.add_new(Contact(midlename="Петрович"))
#    old_con = app.contact.get_con_list()
#    con = Contact(midlename="Михалыч")
#    con.id = old_con[0].id
#    con.firstname = old_con[0].firstname
#    con.lastname = old_con[0].lastname
#    app.contact.edit_1st(con)
#    new_con = app.contact.get_con_list()
#    assert len(old_con) == len(new_con)
#    old_con[0] = con
#    assert sorted(old_con, key=Contact.id_or_max) == sorted(new_con, key=Contact.id_or_max)

#def test_edit_1st_con_lstname(app):
#    if app.contact.count_con() == 0:
#        app.contact.add_new(Contact(lastname="Сидоров"))
#    old_con = app.contact.get_con_list()
#    con = Contact(lastname="Мустафаев")
#    con.id = old_con[0].id
#    con.firstname = old_con[0].firstname
#    app.contact.edit_1st(con)
#    new_con = app.contact.get_con_list()
#    assert len(old_con) == len(new_con)
#    old_con[0] = con
#    assert sorted(old_con, key=Contact.id_or_max) == sorted(new_con, key=Contact.id_or_max)
