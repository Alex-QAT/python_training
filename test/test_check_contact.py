import re

from random import randrange

from fixture.orm import ORMFixture
from model.contact import Contact

#orm = ORMFixture(host="127.0.0.1", db_name="addressbook", user="root", password="b0r0v@Y@")
#orm = ORMFixture(host=host, db_name=db_name, user=user, password=password)

def test_check_every_con_hp_db(app, orm):
    # получаем список контактов с HomePage и сортируем по ID
    l_con_hp = sorted(app.contact.get_con_list(), key=Contact.id_or_max)
    # получаем список контактов из БД и сортируем по ID
    l_con_db = sorted(orm.get_con_list(), key=Contact.id_or_max)
    # Запускаем цикл по списку
    for id in range(app.contact.count_con()):
        con_hp = l_con_hp[id]
        con_db = l_con_db[id]
        #Отладочный вывод некоторых данных из отсортированных списков
        #print(' ')
        #print(' ')
        #print(con_hp.id, con_hp.firstname, con_hp.lastname, con_hp.address)
        #print (' ')
        #print(con_db.id, con_db.firstname, con_db.lastname, con_db.address)
        #print('============')
        # сравниваем поле firstname
        assert con_hp.firstname == con_db.firstname
        # сравниваем поле lastname
        assert con_hp.lastname == con_db.lastname
        # сравниваем поле address
        assert con_hp.address == con_db.address
        # сравниваем данные с HP общая ячейка с телефонами и склеенная строка с телефонами из БД
        assert con_hp.all_phones_hp == merge_phones_hp(con_db)
        # сравниваем данные с HP общая ячейка с email'ами и склеенная, очищенная, отфильтрованная строка с email'ами из БД
        assert con_hp.all_emails_hp == merge_emails_hp(con_db)


def test_check_contact(app):
    index = randrange(app.contact.count_con())
    con_from_hp = app.contact.get_con_list()[index]
    con_from_ep = app.contact.get_con_from_ep(index)
    # обратная проверка:
    #берём список с home_page и берём весь текст с телефонами
    #а потом берём склеенный список из телефонов с edit_page
    assert con_from_hp.all_phones_hp == merge_phones_hp(con_from_ep)
    # обратная проверка:
    # берём список с home_page и берём весь текст с email
    # а потом берём склеенный список из email с edit_page
    assert con_from_hp.all_emails_hp == merge_emails_hp(con_from_ep)
    # прямая проверка: извлекаем нужные поля из home_page и из edit_page и сравниваем их
    assert con_from_hp.firstname == con_from_ep.firstname
    assert con_from_hp.lastname == con_from_ep.lastname
    assert con_from_hp.address == con_from_ep.address

#очистка извлечённых строк от символов скобок, пробелов, дефисов
def clear(s):
    return re.sub("[() -]", "", s)

#склейка всех телефонов с edit_page: извлекаем телефоны, отфильтровываем те которые не None, чистим от скобок, пробелов и дефисов, отфильтровываем которые не пустые.
def merge_phones_hp(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work]))))

#склейка всех email с edit_page: извлекаем телефоны, отфильтровываем те которые не None, отфильтровываем которые не пустые.
def merge_emails_hp(contact):
    return "\n".join(filter(lambda x: x != "",
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3])))


# прямая проверка: извлекаем нужные поля из view_page и из edit_page и сравниваем их
#def test_phone_on_vp(app):
#    index = randrange(app.contact.count_con())
#    con_from_vp = app.contact.get_con_from_vp(index)
#    con_from_ep = app.contact.get_con_from_ep(index)
#    assert con_from_vp.home == con_from_ep.home
#    assert con_from_vp.work == con_from_ep.work
#    assert con_from_vp.mobile == con_from_ep.mobile
#    assert con_from_vp.fax == con_from_ep.fax