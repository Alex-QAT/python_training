from random import randrange

from model.contact import Contact
import random

def test_del_rnd_con_by_id(app, db, check_ui): #c проверкой списков из UI и удалением по индексу
    # предусловие если контактов нет - то создать
    if len(db.get_con_list()) == 0:
        app.contact.add_new(Contact(firstname="Автандил"))
    # получаем список контактов
    old_con = db.get_con_list()
    contact = random.choice(old_con)
    # метод удаления контакта по id
    app.contact.del_con_by_id(contact.id)
    # сравниваем старый список и счётчик контактов по количеству (в старом списке на 1 больше)
    assert len(old_con) - 1 == app.contact.count_con()
    # получаем новый список контактов
    new_con = db.get_con_list()
    #прибиваем в старом списке первый по списку контакт
    old_con.remove(contact)
    # сравниваем списки по содержимому (должны быть идентичны)
    assert old_con == new_con
    # отключаемая сверка списков, полученных из БД и из UI
    if check_ui:
        assert sorted(new_con, key=Contact.id_or_max) == sorted(app.contact.get_con_list(), key=Contact.id_or_max)

#def test_del_rnd_con_by_index(app): #c проверкой списков из UI и удалением по индексу
#    # предусловие если контактов нет - то создать
#    if app.contact.count_con() == 0:
#        app.contact.add_new(Contact(firstname="Автандил"))
#    # получаем список контактов
#    old_con = app.contact.get_con_list()
#    index = randrange(len(old_con))
#    # метод удаления контакта по индексу
#    app.contact.del_con_by_index(index)
#    # сравниваем старый список и счётчик контактов по количеству (в старом списке на 1 больше)
#    assert len(old_con) - 1 == app.contact.count_con()
#    # получаем новый список контактов
#    new_con = app.contact.get_con_list()
#    #прибиваем в старом списке первый по списку контакт
#    old_con[index:index+1] = []
#    # сравниваем списки по содержимому (должны быть идентичны)
#    assert old_con == new_con

#def test_del_1st_con(app):
#    # предусловие если контактов нет - то создать
#    if app.contact.count_con() == 0:
#        app.contact.add_new(Contact(firstname="Автандил"))
#    # получаем список контактов
#    old_con = app.contact.get_con_list()
#    # метод удаления первого в списке контакта
#    app.contact.del_1st_con()
#    # сравниваем старый список и счётчик контактов по количеству (в старом списке на 1 больше)
#    assert len(old_con) - 1 == app.contact.count_con()
#    # получаем новый список контактов
#    new_con = app.contact.get_con_list()
#    #прибиваем в старом списке первый по списку контакт
#    old_con[0:1] = []
#    # сравниваем списки по содержимому (должны быть идентичны)
#    assert old_con == new_con