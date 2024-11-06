from model.contact import Contact


def test_edit_1st_con(app):
    if app.contact.count_con() == 0:
        app.contact.add_new(Contact(firstname="Петя", bday="12", bmonth="September", byear="1981",
                             aday="12", amonth="January", ayear="2025", bmonth_x="'September'", aday_x="14", amonth_x="3"))
    app.contact.edit_1st(Contact(u"Вася", u"Иванович", u"Васильев", "Peter",
                             u"Начальник отдела продаж", u"Grass", u"Волгоград, Аллея героев 23",
                             "+7-495-536-18-27", "+7-917-568-44-45", "+7-988-332-11-25", "4-05-18", "peterpen@mail.ru",
                             "peterpen2@mail.ru", "peterpen3@mail.ru", "www.vk.com/peter_1st", "12", "September", "1981",
                             "12", "January", "2025", "'September'", "14", "3"))


def test_edit_1st_con_firstname(app):
    if app.contact.count_con() == 0:
        app.contact.add_new(Contact(firstname="Петя", bday="12", bmonth="September", byear="1981",
                             aday="12", amonth="January", ayear="2025", bmonth_x="'September'", aday_x="14", amonth_x="3"))
    app.contact.edit_1st(Contact(firstname="Сергей", bday="12", bmonth="September", byear="1981",
                             aday="12", amonth="January", ayear="2025", bmonth_x="'September'", aday_x="14", amonth_x="3"))
