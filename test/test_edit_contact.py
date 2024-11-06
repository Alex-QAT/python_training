from model.contact import Contact


def test_edit_1st_con(app):
    app.contact.edit_1st(Contact(u"Пётр", u"Иванович", u"Васильев", "Peter",
                             u"Начальник отдела продаж", u"Grass", u"Волгоград, Аллея героев 23",
                             "+7-495-536-18-27", "+7-917-568-44-45", "+7-988-332-11-25", "4-05-18", "peterpen@mail.ru",
                             "peterpen2@mail.ru", "peterpen3@mail.ru", "www.vk.com/peter_1st", "12", "September", "1981",
                             "12", "January", "2025", "'September'", "14", "3"))
