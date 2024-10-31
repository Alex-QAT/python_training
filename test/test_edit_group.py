from model.group import Group


def test_edit_1st_group(app):
    app.session.login("admin", "secret")
    app.group.edit_1st(Group("!Начальники", "что-то написать", "что-то шрлмавлд"))
    app.session.logout()