from model.contact import Contact


def test_del_1st_con(app):
    #app.session.login("admin", "secret")
    if app.contact.count_con() == 0:
        app.contact.add_new(Contact(firstname="Автандил"))
    app.contact.del_1st_con()
    #app.session.logout()