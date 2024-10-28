

def test_del_1st_gr(app):
    app.session.login("admin", "secret")
    app.group.del_1st_gr()
    app.session.logout()