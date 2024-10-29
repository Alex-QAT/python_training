from model.group import Group


def test_add_group(app):
    app.session.login("admin", "secret")
    app.group.create(Group("!Начальники", "что-то написать", "что-то шрлмавлд"))
    app.session.logout()