from model.contact import Contact


def test_edit_1st_con(app):
    if app.contact.count_con() == 0:
        app.contact.add_new(Contact(firstname="Петя"))
    old_con = app.contact.get_con_list()
    app.contact.edit_1st(Contact(u"Вася", u"Иванович", u"Васильев", "Peter",
                             u"Начальник отдела продаж", u"Grass", u"Волгоград, Аллея героев 23",
                             "+7-495-536-18-27", "+7-917-568-44-45", "+7-988-332-11-25", "4-05-18", "peterpen@mail.ru",
                             "peterpen2@mail.ru", "peterpen3@mail.ru", "www.vk.com/peter_1st", "12", "September", "1981",
                             "12", "January", "2025"))
    new_con = app.contact.get_con_list()
    assert len(old_con) == len(new_con)


def test_edit_1st_con_firstname(app):
    if app.contact.count_con() == 0:
        app.contact.add_new(Contact(firstname="Петя"))
    old_con = app.contact.get_con_list()
    app.contact.edit_1st(Contact(firstname="Сергей"))
    new_con = app.contact.get_con_list()
    assert len(old_con) == len(new_con)

def test_edit_1st_con_mdlname(app):
    if app.contact.count_con() == 0:
        app.contact.add_new(Contact(midlename="Петрович"))
    old_con = app.contact.get_con_list()
    app.contact.edit_1st(Contact(midlename="Михалыч"))
    new_con = app.contact.get_con_list()
    assert len(old_con) == len(new_con)

def test_edit_1st_con_lstname(app):
    if app.contact.count_con() == 0:
        app.contact.add_new(Contact(lastname="Сидоров"))
    old_con = app.contact.get_con_list()
    app.contact.edit_1st(Contact(lastname="Мустафаев"))
    new_con = app.contact.get_con_list()
    assert len(old_con) == len(new_con)
