from model.group import Group


def test_edit_1st_group_full(app):
    if app.group.count_gr() == 0:
        app.group.create(Group("test-group"))
    old_groups = app.group.get_gr_list()
    app.group.edit_1st(Group(name="!Начальники", header="что-то написать", footer="что-то шрлмавлд"))
    new_groups = app.group.get_gr_list()
    assert len(old_groups) == len(new_groups)


def test_edit_1st_group_name(app):
    if app.group.count_gr() == 0:
        app.group.create(Group("test-group"))
    old_groups = app.group.get_gr_list()
    app.group.edit_1st(Group(name="New Name_Group" ))
    new_groups = app.group.get_gr_list()
    assert len(old_groups) == len(new_groups)


def test_edit_1st_group_header(app):
    if app.group.count_gr() == 0:
        app.group.create(Group("test-group"))
    old_groups = app.group.get_gr_list()
    app.group.edit_1st(Group(header="New Header"))
    new_groups = app.group.get_gr_list()
    assert len(old_groups) == len(new_groups)


def test_edit_1st_group_footer(app):
    if app.group.count_gr() == 0:
        app.group.create(Group("test-group"))
    old_groups = app.group.get_gr_list()
    app.group.edit_1st(Group(footer="New Footer"))
    new_groups = app.group.get_gr_list()
    assert len(old_groups) == len(new_groups)
