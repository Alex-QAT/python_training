from random import randrange
# обратная проверка:
#берём список с home_page и берём весь текст с email
#а потом берём склеенный список из email с edit_page
def test_emails_on_hp(app):
    index = randrange(app.contact.count_con())
    con_from_hp = app.contact.get_con_list()[index]
    con_from_ep = app.contact.get_con_from_ep(index)
    assert con_from_hp.all_emails_hp == merge_emails_hp(con_from_ep)


#склейка всех телефонов с edit_page: извлекаем телефоны, отфильтровываем те которые не None, отфильтровываем которые не пустые.
def merge_emails_hp(contact):
    return "\n".join(filter(lambda x: x != "",
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3])))