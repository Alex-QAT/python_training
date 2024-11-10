from model.contact import Contact


def test_del_1st_con(app):
    #app.session.login("admin", "secret")
    if app.contact.count_con() == 0:
        app.contact.add_new(Contact(firstname="Автандил"))
    old_con = app.contact.get_con_list()
    app.contact.del_1st_con()
    new_con = app.contact.get_con_list()
    assert len(old_con) - 1 == len(new_con)
    old_con[0:1] = []
    assert old_con == new_con
    #app.session.logout()