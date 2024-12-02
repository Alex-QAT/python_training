from model.group import Group


def test_gr_list(app, db):
    ui_list = app.group.get_gr_list()
    def clean(group):
        return Group(id=group.id,name=group.name.strip())
    db_list = map(clean, db.get_gr_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)