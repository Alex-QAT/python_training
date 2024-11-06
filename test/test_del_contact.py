from model.contact import Contact


def test_del_1st_con(app):
    #app.session.login("admin", "secret")
    if app.contact.count_con() == 0:
        app.contact.add_new(Contact(firstname="Петя", bday="12", bmonth="September", byear="1981",
                             aday="12", amonth="January", ayear="2025", bmonth_x="'September'", aday_x="14", amonth_x="3"))
    app.contact.del_1st_con()
    #app.session.logout()