import re
from random import randrange
# обратная проверка:
#берём список с home_page и берём весь текст с телефонами
#а потом берём склеенный список из телефонов с edit_page
def test_phones_on_hp(app):
    index = randrange(app.contact.count_con())
    con_from_hp = app.contact.get_con_list()[index]
    con_from_ep = app.contact.get_con_from_ep(index)
    assert con_from_hp.all_phones_hp == merge_phones_hp(con_from_ep)

# прямая проверка: извлекаем нужные поля из view_page и из edit_page и сравниваем их
def test_phone_on_vp(app):
    index = randrange(app.contact.count_con())
    con_from_vp = app.contact.get_con_from_vp(index)
    con_from_ep = app.contact.get_con_from_ep(index)
    assert con_from_vp.home == con_from_ep.home
    assert con_from_vp.work == con_from_ep.work
    assert con_from_vp.mobile == con_from_ep.mobile
    assert con_from_vp.fax == con_from_ep.fax

def clear(s):
    return re.sub("[() -]", "", s)

#склейка всех телефонов с edit_page: извлекаем телефоны, отфильтровываем те которые не None, чистим от скобок, пробелов и дефисов, отфильтровываем которые не пустые.
def merge_phones_hp(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work]))))