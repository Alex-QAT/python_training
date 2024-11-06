from model.group import Group


def test_del_1st_gr(app):
    if app.group.count_gr() == 0:
        app.group.create(Group("test-group", "бла бла бла", "ту ту ту"))
    app.group.del_1st_gr()
