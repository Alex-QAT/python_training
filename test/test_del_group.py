from model.group import Group


def test_del_1st_gr(app):
    if app.group.count_gr() == 0:
        app.group.create(Group("test-group", "бла бла бла", "ту ту ту"))
    old_groups = app.group.get_gr_list()
    app.group.del_1st_gr()
    new_groups = app.group.get_gr_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups
