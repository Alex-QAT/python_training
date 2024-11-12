from random import randrange

from model.contact import Contact


def test_del_con_by_index(app):
    # предусловие если контактов нет - то создать
    if app.contact.count_con() == 0:
        app.contact.add_new(Contact(firstname="Автандил"))
    # получаем список контактов
    old_con = app.contact.get_con_list()
    index = randrange(len(old_con))
    # метод удаления первого в списке контакта
    app.contact.del_con_by_index(index)
    # сравниваем старый список и счётчик контактов по количеству (в старом списке на 1 больше)
    assert len(old_con) - 1 == app.contact.count_con()
    # получаем новый список контактов
    new_con = app.contact.get_con_list()
    #прибиваем в старом списке первый по списку контакт
    old_con[index:index+1] = []
    # сравниваем списки по содержимому (должны быть идентичны)
    assert old_con == new_con

def test_del_1st_con(app):
    # предусловие если контактов нет - то создать
    if app.contact.count_con() == 0:
        app.contact.add_new(Contact(firstname="Автандил"))
    # получаем список контактов
    old_con = app.contact.get_con_list()
    # метод удаления первого в списке контакта
    app.contact.del_1st_con()
    # сравниваем старый список и счётчик контактов по количеству (в старом списке на 1 больше)
    assert len(old_con) - 1 == app.contact.count_con()
    # получаем новый список контактов
    new_con = app.contact.get_con_list()
    #прибиваем в старом списке первый по списку контакт
    old_con[0:1] = []
    # сравниваем списки по содержимому (должны быть идентичны)
    assert old_con == new_con