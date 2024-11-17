from random import randrange

# прямая проверка: извлекаем нужные поля из home_page и из edit_page и сравниваем их
def test_address_on_hp(app):
    index = randrange(app.contact.count_con())
    con_from_hp = app.contact.get_con_list()[index]
    con_from_ep = app.contact.get_con_from_ep(index)
    assert con_from_hp.address == con_from_ep.address